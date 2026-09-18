"""
Database access service for TO BE platform.
Provides unified Supabase PostgreSQL operations with seamless local fallback persistence.
"""

import os
import uuid
import datetime
import logging
from typing import Dict, Any, List, Optional
import streamlit as st

from data.seed_data import CAREERS_SEED, CAREER_CATEGORIES
from utils.formatting import format_date_human

logger = logging.getLogger(__name__)

def get_secret(key: str, default: Any = None) -> Any:
    """Retrieve secret safely."""
    try:
        if hasattr(st, "secrets") and key in st.secrets:
            return st.secrets[key]
    except Exception:
        pass
    return os.environ.get(key, default)

class DatabaseService:
    def __init__(self):
        self.supabase_url = get_secret("SUPABASE_URL", "")
        self.supabase_key = get_secret("SUPABASE_KEY", "")
        self.is_connected = False
        self.client = None

        if self.supabase_url and self.supabase_key and "your-project-ref" not in self.supabase_url:
            try:
                from supabase import create_client, Client
                self.client: Client = create_client(self.supabase_url, self.supabase_key)
                self.is_connected = True
                logger.info("Connected to Supabase successfully.")
            except Exception as e:
                logger.warning(f"Failed to initialize Supabase client: {e}. Running in local storage mode.")
                self.is_connected = False

        # Initialize local storage cache in session state if needed
        self._init_local_storage()

    def _init_local_storage(self):
        """Ensure session state structures exist for local persistence."""
        if "local_db" not in st.session_state:
            st.session_state["local_db"] = {
                "profiles": {},
                "assessments": {},
                "assessment_results": {},
                "career_selections": {},
                "roadmaps": {},
                "roadmap_phases": {},
                "roadmap_items": {},
                "chat_sessions": {},
                "chat_messages": {}
            }

    # =========================================================================
    # CAREERS & CATEGORIES (Knowledge Base)
    # =========================================================================
    def get_categories(self) -> List[Dict[str, Any]]:
        """Retrieve all career categories."""
        if self.is_connected:
            try:
                res = self.client.table("career_categories").select("*").execute()
                if res.data and len(res.data) > 0:
                    return res.data
            except Exception as e:
                logger.warning(f"Supabase get_categories failed: {e}")
        return CAREER_CATEGORIES

    def get_careers(self, category_id: Optional[str] = None, search_query: Optional[str] = None) -> List[Dict[str, Any]]:
        """Retrieve careers with optional category and search filtering."""
        careers = CAREERS_SEED
        if self.is_connected:
            try:
                query = self.client.table("careers").select("*")
                if category_id and category_id != "all":
                    query = query.eq("category_id", category_id)
                res = query.execute()
                if res.data and len(res.data) > 0:
                    careers = res.data
            except Exception as e:
                logger.warning(f"Supabase get_careers failed: {e}")

        # Apply in-memory filtering if needed
        filtered = []
        for c in careers:
            if category_id and category_id != "all" and c.get("category_id") != category_id:
                continue
            if search_query:
                q = search_query.lower().strip()
                title_match = q in c.get("title", "").lower()
                desc_match = q in c.get("description", "").lower()
                skills = [s.lower() for s in c.get("core_skills", []) + c.get("optional_skills", [])]
                skill_match = any(q in s for s in skills)
                if not (title_match or desc_match or skill_match):
                    continue
            filtered.append(c)
        return filtered

    def get_career_by_id(self, career_id: str) -> Optional[Dict[str, Any]]:
        """Retrieve single career by ID."""
        if not career_id:
            return None
        careers = self.get_careers()
        for c in careers:
            if c.get("id") == career_id:
                return c
        return None

    # =========================================================================
    # USER PROFILE & SETTINGS
    # =========================================================================
    def get_profile(self, user_id: str) -> Optional[Dict[str, Any]]:
        """Retrieve user profile."""
        if not user_id:
            return None
        if self.is_connected:
            try:
                res = self.client.table("profiles").select("*").eq("id", user_id).execute()
                if res.data and len(res.data) > 0:
                    return res.data[0]
            except Exception as e:
                logger.warning(f"Supabase get_profile failed: {e}")

        return st.session_state["local_db"]["profiles"].get(user_id)

    def upsert_profile(self, profile_data: Dict[str, Any]) -> bool:
        """Create or update user profile."""
        user_id = profile_data.get("id")
        if not user_id:
            return False

        profile_data["updated_at"] = datetime.datetime.now(datetime.timezone.utc).isoformat()
        if "created_at" not in profile_data:
            profile_data["created_at"] = profile_data["updated_at"]

        if self.is_connected:
            try:
                self.client.table("profiles").upsert(profile_data).execute()
                return True
            except Exception as e:
                logger.warning(f"Supabase upsert_profile failed: {e}")

        # Local fallback
        existing = st.session_state["local_db"]["profiles"].get(user_id, {})
        existing.update(profile_data)
        st.session_state["local_db"]["profiles"][user_id] = existing
        return True

    # =========================================================================
    # ASSESSMENTS & RESULTS
    # =========================================================================
    def save_assessment_submission(self, user_id: str, responses: List[Dict[str, Any]], results: Dict[str, Any]) -> str:
        """Save assessment attempt, individual responses, and calculated profile results."""
        assessment_id = str(uuid.uuid4())
        now = datetime.datetime.now(datetime.timezone.utc).isoformat()

        # Mark previous assessment results as not current for this user
        if self.is_connected:
            try:
                self.client.table("assessment_results").update({"is_current": False}).eq("user_id", user_id).execute()
                
                # Insert assessment
                self.client.table("assessments").insert({
                    "id": assessment_id,
                    "user_id": user_id,
                    "version": "1.0.0",
                    "created_at": now,
                    "updated_at": now
                }).execute()

                # Insert responses
                resp_payload = [
                    {
                        "id": str(uuid.uuid4()),
                        "assessment_id": assessment_id,
                        "question_id": r.get("question_id"),
                        "response_data": r.get("response_data"),
                        "created_at": now
                    }
                    for r in responses
                ]
                if resp_payload:
                    self.client.table("assessment_responses").insert(resp_payload).execute()

                # Insert results
                result_payload = {
                    "id": str(uuid.uuid4()),
                    "assessment_id": assessment_id,
                    "user_id": user_id,
                    "riasec_scores": results.get("riasec_scores", {}),
                    "strengths": results.get("strengths", []),
                    "work_preferences": results.get("work_preferences", []),
                    "career_priorities": results.get("career_priorities", []),
                    "current_skills": results.get("current_skills", []),
                    "matched_careers": results.get("matched_careers", []),
                    "is_current": True,
                    "created_at": now
                }
                self.client.table("assessment_results").insert(result_payload).execute()
                return assessment_id
            except Exception as e:
                logger.warning(f"Supabase save_assessment_submission failed: {e}")

        # Local storage fallback
        st.session_state["local_db"]["assessments"][assessment_id] = {
            "id": assessment_id,
            "user_id": user_id,
            "version": "1.0.0",
            "responses": responses,
            "created_at": now
        }
        
        # Mark other results non-current
        for res in st.session_state["local_db"]["assessment_results"].values():
            if res.get("user_id") == user_id:
                res["is_current"] = False

        res_id = str(uuid.uuid4())
        st.session_state["local_db"]["assessment_results"][res_id] = {
            "id": res_id,
            "assessment_id": assessment_id,
            "user_id": user_id,
            "riasec_scores": results.get("riasec_scores", {}),
            "strengths": results.get("strengths", []),
            "work_preferences": results.get("work_preferences", []),
            "career_priorities": results.get("career_priorities", []),
            "current_skills": results.get("current_skills", []),
            "matched_careers": results.get("matched_careers", []),
            "is_current": True,
            "created_at": now
        }
        return assessment_id

    def get_latest_assessment_result(self, user_id: str) -> Optional[Dict[str, Any]]:
        """Retrieve the user's most recent active assessment result."""
        if not user_id:
            return None

        if self.is_connected:
            try:
                res = self.client.table("assessment_results").select("*").eq("user_id", user_id).eq("is_current", True).order("created_at", desc=True).limit(1).execute()
                if res.data and len(res.data) > 0:
                    return res.data[0]
            except Exception as e:
                logger.warning(f"Supabase get_latest_assessment_result failed: {e}")

        # Local fallback
        matching = [
            r for r in st.session_state["local_db"]["assessment_results"].values()
            if r.get("user_id") == user_id and r.get("is_current")
        ]
        if matching:
            return sorted(matching, key=lambda x: x.get("created_at", ""), reverse=True)[0]
        return None

    def get_assessment_history(self, user_id: str) -> List[Dict[str, Any]]:
        """Retrieve user's historical assessment results for trend exploration."""
        if not user_id:
            return []

        if self.is_connected:
            try:
                res = self.client.table("assessment_results").select("*").eq("user_id", user_id).order("created_at", desc=True).execute()
                if res.data:
                    return res.data
            except Exception as e:
                logger.warning(f"Supabase get_assessment_history failed: {e}")

        # Local fallback
        user_res = [
            r for r in st.session_state["local_db"]["assessment_results"].values()
            if r.get("user_id") == user_id
        ]
        return sorted(user_res, key=lambda x: x.get("created_at", ""), reverse=True)

    # =========================================================================
    # CAREER SELECTION & ROADMAPS
    # =========================================================================
    def save_career_selection(self, user_id: str, career_id: str) -> bool:
        """Record the career chosen by the user."""
        if not user_id or not career_id:
            return False
        now = datetime.datetime.now(datetime.timezone.utc).isoformat()

        if self.is_connected:
            try:
                self.client.table("user_career_selections").update({"is_current": False}).eq("user_id", user_id).execute()
                self.client.table("user_career_selections").insert({
                    "id": str(uuid.uuid4()),
                    "user_id": user_id,
                    "career_id": career_id,
                    "is_current": True,
                    "selected_at": now,
                    "created_at": now
                }).execute()
                return True
            except Exception as e:
                logger.warning(f"Supabase save_career_selection failed: {e}")

        # Local fallback
        for s in st.session_state["local_db"]["career_selections"].values():
            if s.get("user_id") == user_id:
                s["is_current"] = False
        sel_id = str(uuid.uuid4())
        st.session_state["local_db"]["career_selections"][sel_id] = {
            "id": sel_id,
            "user_id": user_id,
            "career_id": career_id,
            "is_current": True,
            "selected_at": now,
            "created_at": now
        }
        return True

    def save_full_roadmap(self, user_id: str, career_id: str, title: str, description: str, phases_data: List[Dict[str, Any]]) -> str:
        """Create and activate a new personalized career roadmap with its phases and actionable tasks."""
        roadmap_id = str(uuid.uuid4())
        now = datetime.datetime.now(datetime.timezone.utc).isoformat()

        # Mark all other user roadmaps as paused
        if self.is_connected:
            try:
                self.client.table("roadmaps").update({"is_active": False, "status": "paused"}).eq("user_id", user_id).execute()

                # Insert roadmap
                self.client.table("roadmaps").insert({
                    "id": roadmap_id,
                    "user_id": user_id,
                    "career_id": career_id,
                    "title": title,
                    "description": description,
                    "status": "active",
                    "is_active": True,
                    "created_at": now,
                    "updated_at": now
                }).execute()

                # Insert phases and items
                for p_idx, phase in enumerate(phases_data):
                    phase_id = str(uuid.uuid4())
                    self.client.table("roadmap_phases").insert({
                        "id": phase_id,
                        "roadmap_id": roadmap_id,
                        "title": phase.get("title", f"Phase {p_idx + 1}"),
                        "description": phase.get("description", ""),
                        "order_index": p_idx,
                        "created_at": now,
                        "updated_at": now
                    }).execute()

                    items_to_insert = []
                    for i_idx, item in enumerate(phase.get("items", [])):
                        items_to_insert.append({
                            "id": str(uuid.uuid4()),
                            "roadmap_id": roadmap_id,
                            "phase_id": phase_id,
                            "title": item.get("title", ""),
                            "description": item.get("description", ""),
                            "type": item.get("type", "skill"),
                            "order_index": i_idx,
                            "status": "not_started",
                            "is_user_created": item.get("is_user_created", False),
                            "estimated_effort": item.get("estimated_effort", ""),
                            "resources": item.get("resources", []),
                            "completed_at": None,
                            "created_at": now,
                            "updated_at": now
                        })
                    if items_to_insert:
                        self.client.table("roadmap_items").insert(items_to_insert).execute()

                return roadmap_id
            except Exception as e:
                logger.warning(f"Supabase save_full_roadmap failed: {e}")

        # Local storage fallback
        for r in st.session_state["local_db"]["roadmaps"].values():
            if r.get("user_id") == user_id:
                r["is_active"] = False
                r["status"] = "paused"

        st.session_state["local_db"]["roadmaps"][roadmap_id] = {
            "id": roadmap_id,
            "user_id": user_id,
            "career_id": career_id,
            "title": title,
            "description": description,
            "status": "active",
            "is_active": True,
            "created_at": now,
            "updated_at": now
        }

        for p_idx, phase in enumerate(phases_data):
            phase_id = str(uuid.uuid4())
            st.session_state["local_db"]["roadmap_phases"][phase_id] = {
                "id": phase_id,
                "roadmap_id": roadmap_id,
                "title": phase.get("title", f"Phase {p_idx + 1}"),
                "description": phase.get("description", ""),
                "order_index": p_idx,
                "created_at": now,
                "updated_at": now
            }
            for i_idx, item in enumerate(phase.get("items", [])):
                item_id = str(uuid.uuid4())
                st.session_state["local_db"]["roadmap_items"][item_id] = {
                    "id": item_id,
                    "roadmap_id": roadmap_id,
                    "phase_id": phase_id,
                    "title": item.get("title", ""),
                    "description": item.get("description", ""),
                    "type": item.get("type", "skill"),
                    "order_index": i_idx,
                    "status": "not_started",
                    "is_user_created": item.get("is_user_created", False),
                    "estimated_effort": item.get("estimated_effort", ""),
                    "resources": item.get("resources", []),
                    "completed_at": None,
                    "created_at": now,
                    "updated_at": now
                }

        return roadmap_id

    def get_active_roadmap(self, user_id: str) -> Optional[Dict[str, Any]]:
        """Fetch user's current active roadmap with all its phases and actionable items."""
        if not user_id:
            return None

        if self.is_connected:
            try:
                r_res = self.client.table("roadmaps").select("*").eq("user_id", user_id).eq("is_active", True).limit(1).execute()
                if r_res.data and len(r_res.data) > 0:
                    roadmap = r_res.data[0]
                    p_res = self.client.table("roadmap_phases").select("*").eq("roadmap_id", roadmap["id"]).order("order_index").execute()
                    i_res = self.client.table("roadmap_items").select("*").eq("roadmap_id", roadmap["id"]).order("order_index").execute()

                    phases = p_res.data or []
                    items = i_res.data or []

                    # Nest items inside respective phases
                    for p in phases:
                        p["items"] = [item for item in items if item.get("phase_id") == p["id"]]
                    roadmap["phases"] = phases
                    return roadmap
            except Exception as e:
                logger.warning(f"Supabase get_active_roadmap failed: {e}")

        # Local storage fallback
        active_roadmaps = [
            r for r in st.session_state["local_db"]["roadmaps"].values()
            if r.get("user_id") == user_id and r.get("is_active")
        ]
        if not active_roadmaps:
            return None

        roadmap = active_roadmaps[0]
        phases = [
            p for p in st.session_state["local_db"]["roadmap_phases"].values()
            if p.get("roadmap_id") == roadmap["id"]
        ]
        phases = sorted(phases, key=lambda x: x.get("order_index", 0))

        for p in phases:
            p_items = [
                i for i in st.session_state["local_db"]["roadmap_items"].values()
                if i.get("phase_id") == p["id"]
            ]
            p["items"] = sorted(p_items, key=lambda x: x.get("order_index", 0))

        roadmap_copy = dict(roadmap)
        roadmap_copy["phases"] = phases
        return roadmap_copy

    def get_user_roadmaps(self, user_id: str) -> List[Dict[str, Any]]:
        """Retrieve all roadmaps (active, paused, archived) for this user."""
        if not user_id:
            return []

        if self.is_connected:
            try:
                res = self.client.table("roadmaps").select("*").eq("user_id", user_id).order("created_at", desc=True).execute()
                if res.data:
                    return res.data
            except Exception as e:
                logger.warning(f"Supabase get_user_roadmaps failed: {e}")

        user_roadmaps = [
            r for r in st.session_state["local_db"]["roadmaps"].values()
            if r.get("user_id") == user_id
        ]
        return sorted(user_roadmaps, key=lambda x: x.get("created_at", ""), reverse=True)

    def set_active_roadmap(self, user_id: str, roadmap_id: str) -> bool:
        """Switch active roadmap."""
        if not user_id or not roadmap_id:
            return False

        if self.is_connected:
            try:
                self.client.table("roadmaps").update({"is_active": False, "status": "paused"}).eq("user_id", user_id).execute()
                self.client.table("roadmaps").update({"is_active": True, "status": "active"}).eq("id", roadmap_id).execute()
                return True
            except Exception as e:
                logger.warning(f"Supabase set_active_roadmap failed: {e}")

        for r in st.session_state["local_db"]["roadmaps"].values():
            if r.get("user_id") == user_id:
                if r.get("id") == roadmap_id:
                    r["is_active"] = True
                    r["status"] = "active"
                else:
                    r["is_active"] = False
                    r["status"] = "paused"
        return True

    def update_roadmap_item_status(self, item_id: str, status: str) -> bool:
        """Update a specific roadmap task's status with completion timestamp."""
        now = datetime.datetime.now(datetime.timezone.utc).isoformat()
        completed_at = now if status == "completed" else None

        if self.is_connected:
            try:
                self.client.table("roadmap_items").update({
                    "status": status,
                    "completed_at": completed_at,
                    "updated_at": now
                }).eq("id", item_id).execute()
                return True
            except Exception as e:
                logger.warning(f"Supabase update_roadmap_item_status failed: {e}")

        # Local fallback
        if item_id in st.session_state["local_db"]["roadmap_items"]:
            item = st.session_state["local_db"]["roadmap_items"][item_id]
            item["status"] = status
            item["completed_at"] = completed_at
            item["updated_at"] = now
            return True
        return False

    def add_custom_roadmap_item(self, roadmap_id: str, phase_id: str, title: str, description: str = "") -> Optional[Dict[str, Any]]:
        """Add user-created task to a roadmap phase."""
        item_id = str(uuid.uuid4())
        now = datetime.datetime.now(datetime.timezone.utc).isoformat()

        payload = {
            "id": item_id,
            "roadmap_id": roadmap_id,
            "phase_id": phase_id,
            "title": title.strip(),
            "description": description.strip(),
            "type": "custom",
            "order_index": 99,
            "status": "not_started",
            "is_user_created": True,
            "estimated_effort": "Personal task",
            "resources": [],
            "completed_at": None,
            "created_at": now,
            "updated_at": now
        }

        if self.is_connected:
            try:
                self.client.table("roadmap_items").insert(payload).execute()
                return payload
            except Exception as e:
                logger.warning(f"Supabase add_custom_roadmap_item failed: {e}")

        st.session_state["local_db"]["roadmap_items"][item_id] = payload
        return payload

    def get_latest_assessment(self, user_id: str) -> Optional[Dict[str, Any]]:
        """Alias for get_latest_assessment_result."""
        try:
            return self.get_latest_assessment_result(user_id)
        except Exception as e:
            logger.error(f"Error in get_latest_assessment: {e}")
            return None

    def save_assessment_result(self, user_id: str, results: Dict[str, Any]) -> str:
        """Alias for saving assessment result directly."""
        try:
            return self.save_assessment_submission(user_id, responses=[], results=results)
        except Exception as e:
            logger.error(f"Error in save_assessment_result: {e}")
            return str(uuid.uuid4())

    def get_user_roadmaps(self, user_id: str) -> List[Dict[str, Any]]:
        """Retrieve all roadmaps for a user, or active roadmap as list."""
        try:
            active = self.get_active_roadmap(user_id)
            return [active] if active else []
        except Exception as e:
            logger.error(f"Error in get_user_roadmaps: {e}")
            return []

    def save_roadmap(self, user_id: str, roadmap: Dict[str, Any]) -> str:
        """Alias for save_full_roadmap."""
        try:
            return self.save_full_roadmap(
                user_id=user_id,
                career_id=roadmap.get("career_id", "career"),
                title=roadmap.get("title", "Career Roadmap"),
                description=roadmap.get("description", ""),
                phases_data=roadmap.get("phases", [])
            )
        except Exception as e:
            logger.error(f"Error in save_roadmap: {e}")
            return str(uuid.uuid4())

    def delete_user_account(self, user_id: str) -> bool:
        """Permanently delete user profile and cascade delete all associated data."""
        if not user_id:
            return False

        if self.is_connected:
            try:
                self.client.table("profiles").delete().eq("id", user_id).execute()
                return True
            except Exception as e:
                logger.warning(f"Supabase delete_user_account failed: {e}")

        # Local storage cleanup
        for table in ["profiles", "assessments", "assessment_results", "career_selections", "roadmaps", "chat_sessions"]:
            keys_to_del = [k for k, v in st.session_state["local_db"][table].items() if v.get("user_id") == user_id or v.get("id") == user_id]
            for k in keys_to_del:
                del st.session_state["local_db"][table][k]

        return True

# Singleton instance
db_service = DatabaseService()
