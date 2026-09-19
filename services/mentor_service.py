"""
TOBE AI Career Companion service.
Provides grounded, empathetic career counseling with user profile, RAG knowledge retrieval,
multi-turn context resolution, response quality evaluation, and observability tracing.
Zero markdown bold formatting (no ** syntax).
"""

import time
import logging
from typing import Dict, Any, List, Optional
from config import AI_MENTOR_NAME, PROJECT_NAME
from services.llm_service import llm_service, clean_no_bold
from services.database import db_service
from services.conversation import conversation_manager
from services.context_builder import context_builder
from services.career_retrieval import career_retrieval_service
from services.response_evaluator import response_evaluator
from services.suggestions import suggestion_service
from services.tracing import tracer
from utils.security import scrub_pii_for_ai, sanitize_chat_prompt

logger = logging.getLogger(__name__)

class MentorService:
    def __init__(self):
        self.llm = llm_service
        self.db = db_service
        self.conv_mgr = conversation_manager
        self.context_builder = context_builder
        self.retrieval_svc = career_retrieval_service
        self.evaluator = response_evaluator
        self.suggestions = suggestion_service
        self.tracer = tracer

    def get_prompt_starters(self) -> List[str]:
        """Return thoughtful conversation starters for user exploration."""
        return [
            "Is it easy to become a programmer?",
            "What does a UX designer actually do all day?",
            "What if I am not confident in math?",
            "How do I choose between UX Design and Front-End Development?",
            "What skills should I learn first?"
        ]

    def generate_mentor_reply(
        self,
        user_id: str,
        message: str,
        chat_history: List[Dict[str, str]],
        career_override: Optional[Dict[str, Any]] = None
    ) -> str:
        """
        Orchestrates full conversational pipeline:
        User Message -> Context Retrieval -> LLM Generation -> Quality Evaluation -> Final Sanitization -> Tracing.
        """
        start_time = time.time()
        sanitized_msg = sanitize_chat_prompt(message)
        if not sanitized_msg:
            return "How can I help you think through your career path today?"

        # 1. Gather raw user context safely
        profile_rec = self.db.get_latest_assessment_result(user_id) or {}
        user_prof = self.db.get_profile(user_id) or {}
        active_roadmap = self.db.get_active_roadmap(user_id)
        
        active_career = career_override or {}
        progress_info = {}
        if active_roadmap and not active_career:
            active_career = self.db.get_career_by_id(active_roadmap.get("career_id")) or {}
            total = sum(len(p.get("items", [])) for p in active_roadmap.get("phases", []))
            completed = sum(1 for p in active_roadmap.get("phases", []) for i in p.get("items", []) if i.get("status") == "completed")
            pct = int((completed / total * 100)) if total > 0 else 0
            progress_info = {"overall_percentage": pct, "completed_count": completed, "total_count": total}

        user_context = {
            "preferred_name": user_prof.get("preferred_name", "Explorer"),
            "profile": profile_rec,
            "active_career": active_career,
            "roadmap_progress": progress_info
        }

        # 2. Build selective prompt context and RAG facts
        context_pack = self.context_builder.build_prompt_context(
            query=sanitized_msg,
            chat_history=chat_history,
            user_context=user_context,
            page_career=active_career
        )
        system_prompt = self.context_builder.build_system_instruction(context_pack)

        # 3. Construct prompt turns
        formatted_history = context_pack.get("formatted_history", "")
        if formatted_history:
            full_user_prompt = f"{formatted_history}\nUser: {sanitized_msg}\n{AI_MENTOR_NAME}:"
        else:
            full_user_prompt = f"User: {sanitized_msg}\n{AI_MENTOR_NAME}:"

        # 4. Generate initial response
        raw_response = self.llm.generate_text(system_prompt=system_prompt, user_prompt=full_user_prompt)
        clean_reply = clean_no_bold(raw_response)

        # 5. Response Quality Evaluation
        eval_result = self.evaluator.evaluate_response(
            user_query=sanitized_msg,
            generated_response=clean_reply,
            career_context=context_pack.get("active_career_title")
        )

        # 6. Corrective regeneration loop if evaluation fails
        if not eval_result.get("answers_question") or eval_result.get("too_generic") or not eval_result.get("relevant"):
            logger.info(f"Response evaluation triggered corrective regeneration: {eval_result.get('reason')}")
            corrective_instruction = self.evaluator.build_corrective_instruction(sanitized_msg, eval_result)
            corrected_system_prompt = f"{system_prompt}\n\nCRITICAL FIX: {corrective_instruction}"
            raw_response = self.llm.generate_text(system_prompt=corrected_system_prompt, user_prompt=full_user_prompt)
            clean_reply = clean_no_bold(raw_response)
            eval_result = self.evaluator.evaluate_response(sanitized_msg, clean_reply, context_pack.get("active_career_title"))

        # 7. Generate decoupled suggestions (post-response only)
        follow_up_chips = self.suggestions.generate_follow_ups(
            user_query=sanitized_msg,
            response_text=clean_reply,
            active_career=context_pack.get("active_career_title")
        )

        # 8. Record Observability Trace
        latency_ms = (time.time() - start_time) * 1000.0
        self.tracer.trace_turn(
            user_message=sanitized_msg,
            conversation_history=chat_history,
            career_context=active_career,
            user_context=user_context,
            retrieved_knowledge=context_pack.get("retrieved_facts", []),
            final_model_input=sanitized_msg,
            raw_model_output=raw_response,
            evaluation_result=eval_result,
            final_response=clean_reply,
            latency_ms=latency_ms,
            routing_mode=self.llm.provider if self.llm.gemini_key else "Conversational Intelligence Engine",
            fallback_used=not bool(self.llm.gemini_key)
        )

        return clean_reply

# Singleton instance
mentor_service = MentorService()
