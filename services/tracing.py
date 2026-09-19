"""
Observability and tracing service for TOBE AI Career Mentor.
Supports LangSmith tracing when configured via environment/secrets,
with robust local development telemetry for latency, inputs, RAG retrieval,
evaluator verdicts, and final outputs.
"""

import os
import time
import json
import logging
from typing import Dict, Any, Optional, List
import streamlit as st

logger = logging.getLogger(__name__)

def get_config_val(key: str, default: Any = None) -> Any:
    """Retrieve config from Streamlit secrets or OS environment."""
    try:
        if hasattr(st, "secrets") and key in st.secrets:
            return st.secrets[key]
    except Exception:
        pass
    return os.environ.get(key, default)

class MentorTracer:
    def __init__(self):
        self.langsmith_enabled = (
            str(get_config_val("LANGCHAIN_TRACING_V2", "false")).lower() in ["true", "1", "yes"]
            and bool(get_config_val("LANGCHAIN_API_KEY", ""))
        )
        self.project_name = get_config_val("LANGCHAIN_PROJECT", "tobe-career-mentor")
        self.client = None

        if self.langsmith_enabled:
            try:
                from langsmith import Client
                self.client = Client(api_key=get_config_val("LANGCHAIN_API_KEY"))
                logger.info(f"LangSmith tracing initialized for project: {self.project_name}")
            except ImportError:
                logger.warning("langsmith package not installed; falling back to local tracing.")
                self.langsmith_enabled = False
            except Exception as e:
                logger.warning(f"Failed to initialize LangSmith client: {e}; falling back to local tracing.")
                self.langsmith_enabled = False

    def trace_turn(
        self,
        user_message: str,
        conversation_history: List[Dict[str, str]],
        career_context: Optional[Dict[str, Any]],
        user_context: Optional[Dict[str, Any]],
        retrieved_knowledge: List[str],
        final_model_input: str,
        raw_model_output: str,
        evaluation_result: Dict[str, Any],
        final_response: str,
        latency_ms: float,
        routing_mode: str,
        fallback_used: bool,
        error: Optional[str] = None
    ) -> Dict[str, Any]:
        """Record and log structured trace data for the turn."""
        trace_data = {
            "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "user_message": user_message,
            "conversation_history_count": len(conversation_history),
            "current_career": career_context.get("title") if career_context else "None",
            "user_context_summary": {
                "preferred_name": user_context.get("preferred_name") if user_context else "Explorer",
                "active_career": user_context.get("active_career", {}).get("title") if user_context else None,
            },
            "retrieved_knowledge_count": len(retrieved_knowledge),
            "final_model_input": final_model_input,
            "raw_model_output": raw_model_output,
            "evaluation_result": evaluation_result,
            "final_response": final_response,
            "latency_ms": round(latency_ms, 2),
            "routing_mode": routing_mode,
            "fallback_used": fallback_used,
            "error": error
        }

        # Send to LangSmith if active
        if self.langsmith_enabled and self.client:
            try:
                self.client.create_run(
                    name="tobe_mentor_turn",
                    run_type="chain",
                    inputs={
                        "user_message": user_message,
                        "history": conversation_history,
                        "career_context": career_context,
                        "user_context": user_context,
                        "retrieved_knowledge": retrieved_knowledge,
                        "final_prompt": final_model_input
                    },
                    outputs={
                        "raw_output": raw_model_output,
                        "evaluation": evaluation_result,
                        "final_response": final_response
                    },
                    project_name=self.project_name,
                    error=error
                )
            except Exception as e:
                logger.warning(f"Failed to submit trace to LangSmith: {e}")

        # Local structured console output
        debug_output = f"""[TOBE DEBUG TRACE]
USER MESSAGE:
{user_message}

CONVERSATION HISTORY:
{json.dumps(conversation_history[-4:] if conversation_history else [], indent=2)}

CURRENT CAREER:
{career_context.get('title') if career_context else 'None'}

RETRIEVED KNOWLEDGE:
{json.dumps(retrieved_knowledge, indent=2)}

EVALUATION RESULT:
{json.dumps(evaluation_result, indent=2)}

FINAL RESPONSE:
{final_response}

ROUTING: {routing_mode} | FALLBACK: {fallback_used} | LATENCY: {round(latency_ms, 1)}ms
"""
        logger.info(debug_output)
        try:
            print(debug_output)
        except UnicodeEncodeError:
            print(debug_output.encode("ascii", errors="replace").decode("ascii"))

        return trace_data

# Singleton instance
tracer = MentorTracer()
