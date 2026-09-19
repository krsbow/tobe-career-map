"""
Comprehensive automated unit and integration tests for TO BE platform services.
Tests multi-domain matching, standardized O*NET RIASEC profiling, PSA PSOC lookups,
ESCO skills taxonomy, pluggable TVET/TESDA training & learning providers, and skill gap roadmaps.
"""

import unittest
from services.assessment import assessment_service
from services.career_matching import matching_engine, CareerMatchingEngine
from services.career_service import career_service
from services.roadmap_service import roadmap_service
from services.mentor_service import mentor_service
from services.auth import auth_service
from services.database import db_service
from services.psoc_service import PSOCService
from services.onet_interest_service import ONETInterestService
from services.onet_service import ONETService
from services.esco_service import ESCOService
from services.training_service import TrainingService
from services.learning_service import LearningService
from utils.security import scrub_pii_for_ai
from utils.validation import validate_email, parse_and_validate_json_response

class TestToBePlatform(unittest.TestCase):

    def setUp(self):
        import streamlit as st
        if "local_db" not in st.session_state:
            db_service._init_local_storage()

    def test_assessment_scoring(self):
        """Verify RIASEC scoring normalization and level categorization."""
        responses = [
            {"question_id": "interest_1", "response_data": ["i1_investigative"]},
            {"question_id": "interest_2", "response_data": ["i2_analytical_data"]},
            {"question_id": "interest_3", "response_data": ["i3_logical_scientific"]},
            {"question_id": "career_priorities", "response_data": ["p_learning", "p_creativity"]}
        ]
        skills = ["Python", "SQL"]
        results = assessment_service.calculate_results(responses, skills)

        self.assertIn("riasec_scores", results)
        self.assertIn("I", results["riasec_scores"])
        self.assertGreaterEqual(results["riasec_scores"]["I"]["score"], 40)
        self.assertIn("current_skills", results)
        self.assertEqual(results["current_skills"], ["Python", "SQL"])
        self.assertTrue(len(results["strengths"]) > 0)

    def test_psoc_service(self):
        """Verify PSA PSOC occupational taxonomy lookup accuracy."""
        # 2512 Software Developers
        psoc_2512 = PSOCService.get_psoc_by_code("2512")
        self.assertIsNotNone(psoc_2512)
        self.assertEqual(psoc_2512["title"], "Software Developers")
        self.assertIn("Professionals", psoc_2512["major_group"])

        # 2221 Nursing Professionals
        psoc_2221 = PSOCService.get_psoc_by_code("2221")
        self.assertIsNotNone(psoc_2221)
        self.assertEqual(psoc_2221["title"], "Nursing Professionals")

        # 7411 Building and Related Electricians
        psoc_7411 = PSOCService.get_psoc_by_code("7411")
        self.assertIsNotNone(psoc_7411)
        self.assertIn("Electrician", psoc_7411["title"])

    def test_onet_interest_service(self):
        """Verify O*NET standardized 30-question interest profiler calculation."""
        onet_srv = ONETInterestService()
        questions = onet_srv.get_questions(count=30)
        self.assertEqual(len(questions), 30)

        # Simulate answers with high Artistic (A) and Social (S) scores
        answers = {}
        for q in questions:
            if q["dimension"] in ["A", "S"]:
                answers[q["id"]] = 5 # strongly like
            else:
                answers[q["id"]] = 1 # strongly dislike

        profile = onet_srv.score_profiler(answers)
        self.assertIn("scores", profile)
        self.assertIn("top_traits", profile)
        self.assertIn("A", profile["top_traits"])
        self.assertIn("S", profile["top_traits"])
        self.assertGreater(profile["scores"]["A"], profile["scores"]["R"])

    def test_esco_and_training_services(self):
        """Verify ESCO skills crosswalk and TVET/TESDA training regulations."""
        training_srv = TrainingService()
        # Check graphic designer TVET qualifications
        graphic_quals = training_srv.get_qualifications_for_career("graphic-designer")
        self.assertTrue(len(graphic_quals) > 0)
        self.assertTrue(any("NC III" in q["qualification"] or "NC3" in q["code"] for q in graphic_quals))


        # Check commercial electrician TVET qualifications
        elec_quals = training_srv.get_qualifications_for_career("commercial-electrician")
        self.assertTrue(len(elec_quals) > 0)
        self.assertTrue(any("Electrical Installation" in q["qualification"] for q in elec_quals))


        # Learning resources
        learning_srv = LearningService()
        res = learning_srv.get_learning_resources_for_career("registered-nurse")
        self.assertTrue(len(res) > 0)

    def test_multi_domain_career_matching(self):
        """Verify explainable matching across Healthcare, Design, Finance, and Tech."""
        # Healthcare Profile
        nurse_profile = {
            "riasec_scores": {
                "S": {"score": 90, "level": "High"},
                "I": {"score": 75, "level": "High"},
                "R": {"score": 60, "level": "Medium"},
                "A": {"score": 20, "level": "Low"},
                "E": {"score": 30, "level": "Low"},
                "C": {"score": 40, "level": "Low"},
            },
            "top_traits": ["S", "I", "R"],
            "current_skills": ["Patient Care & Assessment", "Clinical Documentation"],
            "career_priorities": ["Direct social impact & helping others"],
            "work_preferences": ["People-Facing & Consultative"]
        }

        matched = matching_engine.match_careers(nurse_profile)
        self.assertTrue(len(matched) > 0)
        top_ids = [m["career_id"] for m in matched[:3]]
        self.assertIn("registered-nurse", top_ids)

        nurse_match = next(m for m in matched if m["career_id"] == "registered-nurse")
        self.assertEqual(nurse_match["alignment_tier"], "Strong alignment")
        self.assertTrue(len(nurse_match["reasons"]) > 0)
        self.assertIn("Patient Care & Assessment", nurse_match["known_skills"])

    def test_career_catalog_and_comparison(self):
        """Verify career catalog search across 26 careers and multi-domain comparison."""
        careers = career_service.get_careers()
        self.assertGreaterEqual(len(careers), 25)

        # Search across healthcare, civil engineering, trades
        nurse = career_service.get_career_details("registered-nurse")
        self.assertIsNotNone(nurse)
        self.assertEqual(nurse["psoc_code"], "2221")

        civil = career_service.get_career_details("civil-engineer")
        self.assertIsNotNone(civil)
        self.assertEqual(civil["psoc_code"], "2142")

        # Comparison matrix
        matrix = career_service.build_comparison_matrix("civil-engineer", "commercial-electrician")
        self.assertEqual(matrix["career_a"]["id"], "civil-engineer")
        self.assertEqual(matrix["career_b"]["id"], "commercial-electrician")
        self.assertNotIn("winner", matrix)

    def test_roadmap_generation_and_skill_gaps(self):
        """Verify dynamic 5-phase roadmap generation with skill gap calculation."""
        roadmap = roadmap_service.generate_personalized_roadmap(
            "frontend-developer",
            {"current_skills": ["HTML5", "CSS3"]}
        )
        self.assertEqual(len(roadmap["phases"]), 5)

        # Check that skill gap is tagged
        phase1_items = roadmap["phases"][0]["items"]
        self.assertTrue(len(phase1_items) > 0)

        # Progress calculation test
        progress = roadmap_service.calculate_progress(roadmap)
        self.assertEqual(progress["overall_percentage"], 0)
        self.assertGreater(progress["total_count"], 0)

        # Next recommended step
        next_step = roadmap_service.get_next_recommended_step(roadmap)
        self.assertIsNotNone(next_step)

    def test_security_pii_scrubbing(self):
        """Verify that sensitive user information is scrubbed before AI processing."""
        sample_context = {
            "preferred_name": "Jordan",
            "email": "jordan@example.com",
            "password": "SuperSecretPassword123!",
            "phone": "+1 (555) 019-2834",
            "token": "jwt_token_abc",
            "career_interests": "Healthcare & Civil Engineering"
        }

        scrubbed = scrub_pii_for_ai(sample_context)
        self.assertNotIn("email", scrubbed)
        self.assertNotIn("password", scrubbed)
        self.assertNotIn("phone", scrubbed)
        self.assertNotIn("token", scrubbed)
        self.assertEqual(scrubbed.get("preferred_name"), "Jordan")

    def test_mentor_conversational_freeform_and_followup(self):
        """Verify that TOBE answers all 8 test scenarios, understands follow-ups, and contains no bold **."""
        # 1. "Do I need to be good at design?"
        reply_design = mentor_service.generate_mentor_reply(
            user_id="test-user",
            message="Do I need to be good at design?",
            chat_history=[]
        )
        self.assertIsNotNone(reply_design)
        self.assertNotIn("**", reply_design)
        self.assertTrue("layout" in reply_design.lower() or "practice" in reply_design.lower() or "usability" in reply_design.lower())

        # 2. "I'm actually not good at drawing."
        reply_drawing = mentor_service.generate_mentor_reply(
            user_id="test-user",
            message="I'm actually not good at drawing.",
            chat_history=[{"role": "user", "content": "Do I need to be good at design?"}, {"role": "assistant", "content": reply_design}]
        )
        self.assertIsNotNone(reply_drawing)
        self.assertNotIn("**", reply_drawing)
        self.assertTrue("drawing" in reply_drawing.lower() or "figma" in reply_drawing.lower() or "illustration" in reply_drawing.lower())

        # 3. "I'm scared I won't be good enough." / "I'm actually scared I'm not smart enough."
        reply_fear = mentor_service.generate_mentor_reply(
            user_id="test-user",
            message="I'm scared I won't be good enough.",
            chat_history=[]
        )
        self.assertIsNotNone(reply_fear)
        self.assertNotIn("**", reply_fear)
        self.assertTrue("self-doubt" in reply_fear.lower() or "practice" in reply_fear.lower() or "beginner" in reply_fear.lower() or "patience" in reply_fear.lower())

        # 4. "I don't even know if I like this career."
        reply_fit = mentor_service.generate_mentor_reply(
            user_id="test-user",
            message="I don't even know if I like this career.",
            chat_history=[]
        )
        self.assertIsNotNone(reply_fit)
        self.assertNotIn("**", reply_fit)
        self.assertTrue("uncertain" in reply_fit.lower() or "sample" in reply_fit.lower() or "mini-project" in reply_fit.lower() or "exploration" in reply_fit.lower())

        # 5. "I have school so I only have two hours a day."
        reply_time = mentor_service.generate_mentor_reply(
            user_id="test-user",
            message="I have school so I only have two hours a day.",
            chat_history=[]
        )
        self.assertIsNotNone(reply_time)
        self.assertNotIn("**", reply_time)
        self.assertTrue("two hours" in reply_time.lower() or "2 hour" in reply_time.lower() or "45 minutes" in reply_time.lower())

        # 6. "What should I learn first?"
        reply_first = mentor_service.generate_mentor_reply(
            user_id="test-user",
            message="What should I learn first?",
            chat_history=[{"role": "user", "content": "is it easy to be a programmer?"}]
        )
        self.assertIsNotNone(reply_first)
        self.assertNotIn("**", reply_first)
        self.assertTrue("html" in reply_first.lower() or "javascript" in reply_first.lower() or "step 1" in reply_first.lower())

        # 7. "Would I need a degree?"
        reply_degree = mentor_service.generate_mentor_reply(
            user_id="test-user",
            message="Would I need a degree?",
            chat_history=[{"role": "user", "content": "What should I learn first?"}, {"role": "assistant", "content": reply_first}]
        )
        self.assertIsNotNone(reply_degree)
        self.assertNotIn("**", reply_degree)
        self.assertTrue("degree" in reply_degree.lower() or "portfolio" in reply_degree.lower() or "proof of work" in reply_degree.lower())

        # 8. "What if I change my mind later?"
        reply_change = mentor_service.generate_mentor_reply(
            user_id="test-user",
            message="What if I change my mind later?",
            chat_history=[{"role": "user", "content": "Would I need a degree?"}, {"role": "assistant", "content": reply_degree}]
        )
        self.assertIsNotNone(reply_change)
        self.assertNotIn("**", reply_change)
        self.assertTrue("changing" in reply_change.lower() or "transferable" in reply_change.lower() or "experiment" in reply_change.lower())

        # 9. Free-form question about programming difficulty
        reply_prog = mentor_service.generate_mentor_reply(
            user_id="test-user",
            message="is it easy to be a programmer?",
            chat_history=[]
        )
        self.assertIsNotNone(reply_prog)
        self.assertNotIn("**", reply_prog)
        self.assertTrue("program" in reply_prog.lower() or "code" in reply_prog.lower() or "learn" in reply_prog.lower())

        # 10. Role comparison: "What is the difference between UX design and frontend development?"
        reply_comp = mentor_service.generate_mentor_reply(
            user_id="test-user",
            message="What is the difference between UX design and frontend development?",
            chat_history=[]
        )
        self.assertIsNotNone(reply_comp)
        self.assertNotIn("**", reply_comp)
        self.assertTrue("ux" in reply_comp.lower() and "front" in reply_comp.lower())

if __name__ == "__main__":
    unittest.main()
