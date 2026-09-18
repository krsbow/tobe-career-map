"""
Authentication service for TO BE platform.
Handles Supabase Auth, Google OAuth, session tokens, and multi-tenant isolation.
"""

import uuid
import datetime
import logging
from typing import Optional, Dict, Any, Tuple
import streamlit as st

from services.database import db_service
from utils.validation import validate_email, validate_password_strength

logger = logging.getLogger(__name__)

def is_gmail(email: str) -> bool:
    """Validate if email address ends strictly with @gmail.com."""
    if not email:
        return False
    return email.strip().lower().endswith("@gmail.com")

class AuthService:
    def __init__(self):
        self.db = db_service
        self._init_session()

    def _init_session(self):
        """Ensure session state variables for authentication are set."""
        if "user" not in st.session_state:
            st.session_state["user"] = None
        if "auth_token" not in st.session_state:
            st.session_state["auth_token"] = None

    def get_current_user(self) -> Optional[Dict[str, Any]]:
        """Return currently authenticated user from session state."""
        return st.session_state.get("user")

    def is_authenticated(self) -> bool:
        """Check if a valid user is signed in."""
        user = st.session_state.get("user")
        return user is not None and is_gmail(user.get("email", ""))

    def sign_up(self, email: str, password: str, preferred_name: str, terms_accepted: bool = True) -> Tuple[bool, str]:
        """Register a new user account with Supabase Auth or local demo."""
        email = email.strip().lower()
        if not validate_email(email):
            return False, "Please enter a valid email address."

        # Strict Gmail domain requirement
        if not is_gmail(email):
            return False, "Access restricted: Only @gmail.com accounts are permitted to register."

        valid_pwd, pwd_err = validate_password_strength(password)
        if not valid_pwd:
            return False, pwd_err

        if not terms_accepted:
            return False, "You must acknowledge the Terms of Service to create an account."

        # Supabase Auth
        if self.db.is_connected and self.db.client:
            try:
                res = self.db.client.auth.sign_up({
                    "email": email,
                    "password": password,
                    "options": {
                        "data": {
                            "preferred_name": preferred_name,
                            "full_name": preferred_name
                        }
                    }
                })
                if res.user:
                    user_id = str(res.user.id)
                    user_obj = {
                        "id": user_id,
                        "email": email,
                        "preferred_name": preferred_name or email.split("@")[0]
                    }
                    st.session_state["user"] = user_obj
                    
                    # Create profile record in DB
                    self.db.upsert_profile({
                        "id": user_id,
                        "email": email,
                        "preferred_name": preferred_name,
                        "full_name": preferred_name,
                        "terms_accepted": True,
                        "terms_accepted_at": datetime.datetime.now(datetime.timezone.utc).isoformat()
                    })
                    return True, "Account created successfully!"
            except Exception as e:
                logger.warning(f"Supabase sign_up error: {e}")
                return False, str(e)

        # Local Demo Mode sign up
        user_id = str(uuid.uuid5(uuid.NAMESPACE_DNS, email.lower()))
        user_obj = {
            "id": user_id,
            "email": email,
            "preferred_name": preferred_name or email.split("@")[0]
        }
        st.session_state["user"] = user_obj
        self.db.upsert_profile({
            "id": user_id,
            "email": email,
            "preferred_name": preferred_name,
            "full_name": preferred_name,
            "terms_accepted": True,
            "terms_accepted_at": datetime.datetime.now(datetime.timezone.utc).isoformat()
        })
        return True, "Account created successfully!"

    def sign_in(self, email: str, password: str) -> Tuple[bool, str]:
        """Authenticate user with email and password."""
        email = email.strip().lower()
        if not validate_email(email):
            return False, "Please enter a valid email address."

        if not is_gmail(email):
            return False, "Access restricted: Please use a valid @gmail.com email address."

        # Clear any prior user state before authenticating new user
        self._clear_all_user_session_state()

        if self.db.is_connected and self.db.client:
            try:
                res = self.db.client.auth.sign_in_with_password({
                    "email": email,
                    "password": password
                })
                if res.user:
                    user_id = str(res.user.id)
                    user_metadata = res.user.user_metadata or {}
                    preferred_name = (
                        user_metadata.get("preferred_name")
                        or user_metadata.get("full_name")
                        or email.split("@")[0]
                    )

                    st.session_state["user"] = {
                        "id": user_id,
                        "email": email,
                        "preferred_name": preferred_name
                    }
                    if res.session:
                        st.session_state["auth_token"] = res.session.access_token

                    # Ensure profile exists
                    self.db.upsert_profile({
                        "id": user_id,
                        "email": email,
                        "preferred_name": preferred_name,
                        "updated_at": datetime.datetime.now(datetime.timezone.utc).isoformat()
                    })
                    return True, "Signed in successfully!"
            except Exception as e:
                logger.warning(f"Supabase sign_in error: {e}")
                return False, "Invalid email or password."

        # Local demo login fallback
        user_id = str(uuid.uuid5(uuid.NAMESPACE_DNS, email))
        profile = self.db.get_profile(user_id)
        preferred_name = profile.get("preferred_name") if profile else email.split("@")[0]

        st.session_state["user"] = {
            "id": user_id,
            "email": email,
            "preferred_name": preferred_name
        }
        return True, "Signed in successfully!"

    def sign_in_with_google(self) -> Tuple[bool, str]:
        """Initiate Supabase Google OAuth flow."""
        self._clear_all_user_session_state()
        if self.db.is_connected and self.db.client:
            try:
                res = self.db.client.auth.sign_in_with_oauth({
                    "provider": "google",
                    "options": {
                        "query_params": {
                            "access_type": "offline",
                            "prompt": "select_account"
                        }
                    }
                })
                if res.url:
                    return True, res.url
            except Exception as e:
                logger.warning(f"Supabase Google OAuth error: {e}")
                return False, str(e)

        # Fallback local Google demo
        user_id = str(uuid.uuid4())
        email = "explorer.demo@gmail.com"
        st.session_state["user"] = {
            "id": user_id,
            "email": email,
            "preferred_name": "Google Explorer"
        }
        self.db.upsert_profile({
            "id": user_id,
            "email": email,
            "preferred_name": "Google Explorer",
            "full_name": "Google Explorer"
        })
        return True, "Authenticated with Google Demo"

    def _clear_all_user_session_state(self):
        """Purge all user-specific state to prevent data leakage across accounts."""
        keys_to_clear = [
            "user", "auth_token", "active_roadmap", "assessment_results",
            "saved_careers", "recently_viewed", "career_notes", "chat_history"
        ]
        for k in keys_to_clear:
            if k in st.session_state:
                st.session_state[k] = None

    def sign_out(self):
        """Sign out current user and purge all user-specific session data."""
        if self.db.is_connected and self.db.client:
            try:
                self.db.client.auth.sign_out()
            except Exception as e:
                logger.warning(f"Supabase sign_out error: {e}")

        self._clear_all_user_session_state()

# Singleton instance
auth_service = AuthService()
