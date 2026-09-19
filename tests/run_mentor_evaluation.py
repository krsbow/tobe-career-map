"""
Automated Evaluation Runner for TOBE AI Career Mentor.
Runs all test cases from data/mentor_eval_dataset.json against the mentor service,
evaluates quality metrics, enforces zero markdown bold syntax, and logs benchmark stats.
"""

import sys
import os
import json
import time

# Ensure project root is in sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from services.mentor_service import mentor_service
from services.response_evaluator import response_evaluator

DATASET_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "mentor_eval_dataset.json")

def run_evaluation():
    if not os.path.exists(DATASET_PATH):
        print(f"Error: Evaluation dataset not found at {DATASET_PATH}")
        sys.exit(1)

    with open(DATASET_PATH, "r", encoding="utf-8") as f:
        test_cases = json.load(f)

    print(f"\n=======================================================")
    print(f"  RUNNING TOBE AI MENTOR BENCHMARK EVALUATION ({len(test_cases)} CASES)")
    print(f"=======================================================\n")

    passed = 0
    failed = 0
    results = []

    for idx, test in enumerate(test_cases, 1):
        test_id = test.get("id", f"case_{idx}")
        user_msg = test.get("user_message", "")
        history = test.get("conversation_context", [])
        career_ctx = {"title": test.get("career_context")} if test.get("career_context") else None

        t0 = time.time()
        reply = mentor_service.generate_mentor_reply(
            user_id="eval_user",
            message=user_msg,
            chat_history=history,
            career_override=career_ctx
        )
        latency_ms = (time.time() - t0) * 1000.0

        eval_verdict = response_evaluator.evaluate_response(
            user_query=user_msg,
            generated_response=reply,
            career_context=test.get("career_context")
        )

        has_bold = "**" in reply or "__" in reply
        passes_quality = eval_verdict.get("answers_question") and not eval_verdict.get("too_generic") and not has_bold

        if passes_quality:
            passed += 1
            status_str = "PASSED"
        else:
            failed += 1
            status_str = "FAILED"

        result_entry = {
            "id": test_id,
            "query": user_msg,
            "status": status_str,
            "latency_ms": round(latency_ms, 1),
            "verdict": eval_verdict,
            "reply_sample": reply[:120].replace("\n", " ") + "..."
        }
        results.append(result_entry)

        def safe_print(s):
            try:
                print(s)
            except UnicodeEncodeError:
                print(s.encode("ascii", errors="replace").decode("ascii"))

        safe_print(f"[{status_str}] ({test_id}) {user_msg}")
        if not passes_quality:
            safe_print(f"   Reason: {eval_verdict.get('reason')}")
            safe_print(f"   Reply: {reply[:200]}...")

    print(f"\n=======================================================")
    print(f"  EVALUATION SUMMARY")
    print(f"=======================================================")
    print(f"  Total Cases Evaluated: {len(test_cases)}")
    print(f"  Passed: {passed}")
    print(f"  Failed: {failed}")
    print(f"  Success Rate: {round((passed / len(test_cases)) * 100, 1)}%")
    print(f"=======================================================\n")

    return failed == 0

if __name__ == "__main__":
    success = run_evaluation()
    sys.exit(0 if success else 1)
