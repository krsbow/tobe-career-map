"""
Unit tests for TO BE Guided Career Mentor.
Verifies structured guided discovery, dynamic question progression,
prerequisite adaptation, and grounded answers across 6 core careers.
"""

import unittest
from services.guided_mentor import guided_mentor, GuidedMentorEngine
from data.seed_data import CAREERS_SEED

class TestGuidedMentor(unittest.TestCase):
    def setUp(self):
        self.engine = GuidedMentorEngine()
        self.target_careers = [
            "ai-ml-engineer",
            "ux-designer",
            "cybersecurity-analyst",
            "data-analyst",
            "fullstack-developer",
            "product-manager",
        ]

    def test_initial_questions_structure_across_all_target_careers(self):
        """Verify get_initial_questions returns 3 high-priority questions with category variety."""
        for cid in self.target_careers:
            career = self.engine.get_career(cid)
            self.assertIsNotNone(career, f"Career {cid} should exist in seed database")
            
            initial_qs = self.engine.get_initial_questions(career)
            self.assertEqual(len(initial_qs), 3, f"Initial questions for {cid} should return exactly 3 questions")
            
            categories = {q["category"] for q in initial_qs}
            self.assertIn("WHAT", categories, f"{cid} should include a WHAT question")
            self.assertIn("WHY", categories, f"{cid} should include a WHY question")
            self.assertIn("HOW", categories, f"{cid} should include a HOW question")

    def test_prerequisite_adaptive_wording_and_grounding(self):
        """Verify adaptive prerequisite questions and answers for specific domains."""
        # 1. AI / ML
        ai_career = self.engine.get_career("ai-ml-engineer")
        if ai_career:
            q_ai = self.engine.get_prerequisite_question(ai_career)
            a_ai = self.engine.get_prerequisite_answer(ai_career)
            self.assertIn("math", q_ai.lower())
            self.assertIn("linear algebra", a_ai.lower())

        # 2. UI/UX
        ux_career = self.engine.get_career("ux-designer")
        self.assertIsNotNone(ux_career)
        q_ux = self.engine.get_prerequisite_question(ux_career)
        a_ux = self.engine.get_prerequisite_answer(ux_career)
        self.assertIn("drawing", q_ux.lower())
        self.assertIn("figma", a_ux.lower())

        # 3. Cybersecurity
        sec_career = self.engine.get_career("cybersecurity-analyst")
        self.assertIsNotNone(sec_career)
        q_sec = self.engine.get_prerequisite_question(sec_career)
        a_sec = self.engine.get_prerequisite_answer(sec_career)
        self.assertIn("programming", q_sec.lower())
        self.assertIn("networking", a_sec.lower())

        # 4. Data Analyst
        data_career = self.engine.get_career("data-analyst")
        self.assertIsNotNone(data_career)
        q_data = self.engine.get_prerequisite_question(data_career)
        a_data = self.engine.get_prerequisite_answer(data_career)
        self.assertIn("statistics", q_data.lower())
        self.assertIn("sql", a_data.lower())

        # 5. Project / Product Manager
        pm_career = self.engine.get_career("product-manager")
        if pm_career:
            q_pm = self.engine.get_prerequisite_question(pm_career)
            a_pm = self.engine.get_prerequisite_answer(pm_career)
            self.assertIn("technical", q_pm.lower())
            self.assertIn("agile", a_pm.lower())

    def test_question_progression_and_deduplication(self):
        """Verify questions dynamically update without repeating already-explored intents."""
        career = self.engine.get_career("data-analyst")
        explored = []

        # Step 1: initial questions
        q_step1 = self.engine.get_next_questions(career, explored)
        self.assertEqual(len(q_step1), 3)

        # Pick first question intent
        first_intent = q_step1[0]["intent"]
        explored.append(first_intent)

        # Step 2: next questions should NOT contain first_intent
        q_step2 = self.engine.get_next_questions(career, explored)
        self.assertEqual(len(q_step2), 3)
        self.assertNotIn(first_intent, [q["intent"] for q in q_step2])

        # Pick additional intents until we reach 5 explored
        while len(explored) < 5:
            next_qs = self.engine.get_next_questions(career, explored)
            if not next_qs:
                break
            explored.append(next_qs[0]["intent"])

        # Check completion
        is_complete = self.engine.check_completion(explored)
        self.assertTrue(is_complete, "Engine should flag completion when 5 intents are explored")

    def test_grounded_answer_generation(self):
        """Verify answers contain concrete career data without generic evasion phrases."""
        career = self.engine.get_career("fullstack-developer")
        salary_ans = self.engine.generate_answer("salary", career)
        self.assertIn("₱", salary_ans)
        self.assertIn("Entry-Level", salary_ans)

        tools_ans = self.engine.generate_answer("tools", career)
        self.assertTrue(len(tools_ans) > 20)
        self.assertNotIn("I cannot answer that", tools_ans)
        self.assertNotIn("As an AI", tools_ans)

if __name__ == "__main__":
    unittest.main()
