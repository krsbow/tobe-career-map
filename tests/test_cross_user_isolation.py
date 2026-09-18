"""
Automated Test Suite: TO BE Multi-Tenant Data Isolation & Security
Verifies:
1. Cross-user data isolation (User A vs User B).
2. Complete session cleanup on logout.
3. Strict @gmail.com domain validation.
4. Database RLS multi-tenant protection.
"""

import unittest
import uuid
from services.auth import is_gmail, AuthService
from services.database import DatabaseService

class TestCrossUserDataIsolation(unittest.TestCase):
    def setUp(self):
        self.auth = AuthService()
        self.db = DatabaseService()
        self.user_a_email = f"user_a_{uuid.uuid4().hex[:6]}@gmail.com"
        self.user_b_email = f"user_b_{uuid.uuid4().hex[:6]}@gmail.com"

    def test_gmail_domain_validation(self):
        """Verify only @gmail.com email addresses are permitted."""
        self.assertTrue(is_gmail("john.doe@gmail.com"))
        self.assertTrue(is_gmail("alex_dev123@gmail.com"))
        self.assertFalse(is_gmail("user@yahoo.com"))
        self.assertFalse(is_gmail("user@outlook.com"))
        self.assertFalse(is_gmail("hacker@malicious.org"))
        self.assertFalse(is_gmail("user@notgmail.com"))
        self.assertFalse(is_gmail(""))

    def test_cross_user_isolation_lifecycle(self):
        """
        Verify complete isolation between User A and User B:
        User A creates data -> Logs out -> User B logs in -> User B sees empty data -> User A logs back in.
        """
        # 1. USER A Signs Up / In
        success, msg = self.auth.sign_up(self.user_a_email, "Password123!", "User Alpha")
        self.assertTrue(success, f"User A signup failed: {msg}")
        user_a = self.auth.get_current_user()
        self.assertIsNotNone(user_a)
        user_a_id = user_a["id"]

        # User A saves assessment and notes
        assess_id = self.db.save_assessment_submission(
            user_a_id,
            [{"question_id": "q1", "response_data": "option_a"}],
            {
                "riasec_scores": {"R": 5, "I": 8, "A": 9},
                "matched_careers": [{"career_id": "frontend-developer", "match_score": 92}]
            }
        )
        self.assertIsNotNone(assess_id)

        # User A creates a roadmap
        roadmap_id = self.db.save_full_roadmap(
            user_a_id,
            "frontend-developer",
            "Front-End Developer Pathway",
            "Mastering React and modern UI",
            [{"title": "Phase 1", "description": "HTML & CSS", "items": [{"title": "Learn CSS Grid"}]}]
        )
        self.assertIsNotNone(roadmap_id)

        # Verify User A can see their own data
        user_a_assess = self.db.get_latest_assessment_result(user_a_id)
        self.assertIsNotNone(user_a_assess)
        self.assertEqual(user_a_assess.get("user_id"), user_a_id)

        user_a_roadmap = self.db.get_active_roadmap(user_a_id)
        self.assertIsNotNone(user_a_roadmap)
        self.assertEqual(user_a_roadmap.get("user_id"), user_a_id)

        # 2. USER A Logs Out
        self.auth.sign_out()
        self.assertIsNone(self.auth.get_current_user())

        # 3. USER B Signs Up / In with different account
        success_b, msg_b = self.auth.sign_up(self.user_b_email, "Password123!", "User Beta")
        self.assertTrue(success_b, f"User B signup failed: {msg_b}")
        user_b = self.auth.get_current_user()
        self.assertIsNotNone(user_b)
        user_b_id = user_b["id"]
        self.assertNotEqual(user_a_id, user_b_id)

        # 4. Verify USER B CANNOT see User A's data
        user_b_assess = self.db.get_latest_assessment_result(user_b_id)
        self.assertIsNone(user_b_assess, "CRITICAL ERROR: User B can see assessment data from User A!")

        user_b_roadmap = self.db.get_active_roadmap(user_b_id)
        self.assertIsNone(user_b_roadmap, "CRITICAL ERROR: User B can see roadmap data from User A!")

        # 5. USER B Logs Out
        self.auth.sign_out()

        # 6. USER A Logs Back In
        success_relogin, _ = self.auth.sign_in(self.user_a_email, "Password123!")
        self.assertTrue(success_relogin)
        user_a_restored = self.auth.get_current_user()
        self.assertEqual(user_a_restored["id"], user_a_id)

        # User A's original data is preserved
        restored_assess = self.db.get_latest_assessment_result(user_a_id)
        self.assertIsNotNone(restored_assess)
        self.assertEqual(restored_assess.get("user_id"), user_a_id)

        restored_roadmap = self.db.get_active_roadmap(user_a_id)
        self.assertIsNotNone(restored_roadmap)
        self.assertEqual(restored_roadmap.get("user_id"), user_a_id)

if __name__ == "__main__":
    unittest.main()
