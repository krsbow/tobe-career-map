"""
Comprehensive automated unit and integration tests for TO BE platform services.
"""

import unittest
from services.assessment import assessment_service
from services.career_matching import matching_engine
from services.career_service import career_service
from services.roadmap_service import roadmap_service
from services.mentor_service import mentor_service
from services.auth import auth_service
from services.database import db_service
from utils.security import scrub_pii_for_ai
from utils.validation import validate_email, parse_and_validate_json_response

class TestToBePlatform(unittest.TestCase):

    def setUp(self):
        # Reset local database state in session mock if needed
        import streamlit as st
        if "local_db" not in st.session_state:
            db_service._init_local_storage()

    def test_assessment_scoring(self):
        """Verify RIASEC scoring normalization and level categorization."""
        responses = [
            {"question_id": "interest_1", "response_data": ["i1_investigative"]},
            {"question_id": "interest_2", "response_data": ["i2_investigative_realistic"]},
            {"question_id": "interest_3", "response_data": ["i3_logical_algorithmic"]},
            {"question_id": "career_priorities", "response_data": ["p_learning", "p_creativity"]}
        ]
        skills = ["Python", "SQL"]
        results = assessment_service.calculate_results(responses, skills)

        self.assertIn("riasec_scores", results)
        self.assertIn("I", results["riasec_scores"])
        # Investigative score should be high
        self.assertGreaterEqual(results["riasec_scores"]["I"]["score"], 50)
        self.assertEqual(results["riasec_scores"]["I"]["level"], "High")
        self.assertIn("current_skills", results)
        self.assertEqual(results["current_skills"], ["Python", "SQL"])
        self.assertTrue(len(results["strengths"]) > 0)

    def test_career_matching_non_exclusion(self):
        """Verify that lack of current skills does not disqualify user from a career."""
        mock_profile = {
            "riasec_scores": {
                "I": {"score": 80, "level": "High"},
                "R": {"score": 75, "level": "High"},
                "C": {"score": 60, "level": "High"},
                "A": {"score": 20, "level": "Low"},
                "S": {"score": 20, "level": "Low"},
                "E": {"score": 10, "level": "Low"}
            },
            "top_dimensions": ["I", "R", "C"],
            "current_skills": [], # Zero prior skills
            "career_priorities": ["Continuous Learning"],
            "work_preferences": ["Deep Focus / Independent"]
        }

        matched = matching_engine.match_careers(mock_profile)
        self.assertTrue(len(matched) > 0)

        # Cybersecurity and backend should appear with explanation and what to develop
        career_ids = [m["career_id"] for m in matched]
        self.assertIn("cybersecurity-analyst", career_ids)

        cyber = next(m for m in matched if m["career_id"] == "cybersecurity-analyst")
        self.assertTrue(len(cyber["why_it_appeared"]) > 0)
        self.assertTrue(len(cyber["what_to_develop"]) > 0)

    def test_career_catalog_and_comparison(self):
        """Verify career catalog search and comparison matrix without declaring winner."""
        categories = career_service.get_all_categories()
        self.assertGreaterEqual(len(categories), 5)

        # Search
        results = career_service.get_careers(search_query="React")
        self.assertTrue(any(c["id"] == "frontend-developer" for c in results))

        # Comparison
        matrix = career_service.build_comparison_matrix("frontend-developer", "ux-designer")
        self.assertEqual(matrix["career_a"]["id"], "frontend-developer")
        self.assertEqual(matrix["career_b"]["id"], "ux-designer")
        self.assertNotIn("winner", matrix)
        self.assertTrue(len(matrix["comparison_points"]) >= 6)

    def test_roadmap_generation_and_progress(self):
        """Verify 5-phase roadmap generation and dynamic progress calculation."""
        roadmap = roadmap_service.generate_personalized_roadmap("frontend-developer", {"current_skills": ["HTML"]})
        self.assertEqual(len(roadmap["phases"]), 5)

        # Check phase titles
        self.assertIn("Foundations", roadmap["phases"][0]["title"])
        self.assertIn("Career Ready", roadmap["phases"][4]["title"])

        # Progress calculation test
        progress = roadmap_service.calculate_progress(roadmap)
        self.assertEqual(progress["overall_percentage"], 0)
        self.assertGreater(progress["total_count"], 0)

        # Simulate completed item in phase 0
        roadmap["phases"][0]["items"][0]["status"] = "completed"
        progress_after = roadmap_service.calculate_progress(roadmap)
        self.assertGreater(progress_after["overall_percentage"], 0)
        self.assertEqual(progress_after["completed_count"], 1)

        # Next recommended step
        next_step = roadmap_service.get_next_recommended_step(roadmap)
        self.assertIsNotNone(next_step)
        self.assertIn(next_step["item"]["status"], ["not_started", "in_progress"])

    def test_security_pii_scrubbing(self):
        """Verify that sensitive user information is scrubbed before AI processing."""
        sample_context = {
            "preferred_name": "Jordan",
            "email": "jordan@example.com",
            "password": "SuperSecretPassword123!",
            "phone": "+1 (555) 019-2834",
            "token": "jwt_token_abc",
            "career_interests": "Cybersecurity & Web Development"
        }

        scrubbed = scrub_pii_for_ai(sample_context)
        self.assertNotIn("email", scrubbed)
        self.assertNotIn("password", scrubbed)
        self.assertNotIn("phone", scrubbed)
        self.assertNotIn("token", scrubbed)
        self.assertEqual(scrubbed.get("preferred_name"), "Jordan")
        self.assertEqual(scrubbed.get("career_interests"), "Cybersecurity & Web Development")

    def test_mentor_fallback_reply(self):
        """Verify that TOBE generates supportive advice even with zero API keys configured."""
        reply = mentor_service.generate_mentor_reply(
            user_id="test-user",
            message="I'm interested in cybersecurity but not sure if I'll like it.",
            chat_history=[]
        )
        self.assertIsNotNone(reply)
        self.assertTrue(len(reply) > 50)
        # Verify it doesn't give a dogmatic answer
        self.assertNotIn("You will certainly become", reply)

if __name__ == "__main__":
    unittest.main()
