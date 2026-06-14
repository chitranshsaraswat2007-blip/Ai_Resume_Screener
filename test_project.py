# ============================================================
# test_project.py - Integration Testing Module
# Programmer 4: Testing, Integration & Documentation
# ============================================================
# This file tests all modules together to verify the system
# works correctly end-to-end.
# Run with: python test_project.py
# ============================================================

import sys
import os

# Add project root to the Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from preprocessing.cleaner import clean_text
from ai_engine.similarity import calculate_similarity
from ai_engine.ranking import rank_candidates, get_top_candidates


# ============================================================
# TEST 1: Text Cleaning Module
# ============================================================
def test_clean_text():
    print("\n" + "="*50)
    print("TEST 1: Text Cleaning Module")
    print("="*50)

    raw_text = "Hello! I am John123. Skills: Python, ML & AI @2024."
    cleaned = clean_text(raw_text)

    print(f"Input : {raw_text}")
    print(f"Output: {cleaned}")

    # Verify cleaning rules
    assert cleaned == cleaned.lower(), "FAIL: Text should be lowercase"
    assert not any(c.isdigit() for c in cleaned), "FAIL: Numbers should be removed"
    assert "@" not in cleaned, "FAIL: Special symbols should be removed"

    print("RESULT: PASSED ✅")


# ============================================================
# TEST 2: Empty Text Handling
# ============================================================
def test_empty_text():
    print("\n" + "="*50)
    print("TEST 2: Empty Text Handling")
    print("="*50)

    result = clean_text("")
    print(f"Input : (empty string)")
    print(f"Output: '{result}'")

    assert result == "", "FAIL: Empty input should return empty string"
    print("RESULT: PASSED ✅")


# ============================================================
# TEST 3: Similarity Score - High Match
# ============================================================
def test_high_similarity():
    print("\n" + "="*50)
    print("TEST 3: High Similarity (Related Texts)")
    print("="*50)

    job = "python developer machine learning data science pandas numpy"
    resume = "python machine learning data science developer pandas"

    score = calculate_similarity(job, resume)
    print(f"Job Description : {job}")
    print(f"Resume Text     : {resume}")
    print(f"Similarity Score: {score}%")

    assert score > 50, f"FAIL: Expected high score but got {score}%"
    print("RESULT: PASSED ✅")


# ============================================================
# TEST 4: Similarity Score - Low Match
# ============================================================
def test_low_similarity():
    print("\n" + "="*50)
    print("TEST 4: Low Similarity (Unrelated Texts)")
    print("="*50)

    job = "python developer machine learning data science"
    resume = "graphic designer adobe photoshop illustrator branding"

    score = calculate_similarity(job, resume)
    print(f"Job Description : {job}")
    print(f"Resume Text     : {resume}")
    print(f"Similarity Score: {score}%")

    assert score < 30, f"FAIL: Expected low score but got {score}%"
    print("RESULT: PASSED ✅")


# ============================================================
# TEST 5: Candidate Ranking
# ============================================================
def test_ranking():
    print("\n" + "="*50)
    print("TEST 5: Candidate Ranking")
    print("="*50)

    scores = {
        "Alice": 85.5,
        "Bob": 62.3,
        "Charlie": 91.0,
        "Diana": 47.8
    }

    ranked = rank_candidates(scores)
    print(ranked.to_string(index=False))

    # Verify Charlie is ranked #1 (highest score)
    assert ranked.iloc[0]["Candidate Name"] == "Charlie", "FAIL: Charlie should be rank 1"
    assert ranked.iloc[0]["Rank"] == 1, "FAIL: First row should have Rank 1"
    print("\nRESULT: PASSED ✅")


# ============================================================
# TEST 6: Top Candidates Filter
# ============================================================
def test_top_candidates():
    print("\n" + "="*50)
    print("TEST 6: Top N Candidates")
    print("="*50)

    scores = {
        "Alice": 85.5,
        "Bob": 62.3,
        "Charlie": 91.0,
        "Diana": 47.8,
        "Eve": 78.0
    }

    top2 = get_top_candidates(scores, top_n=2)
    print(top2.to_string(index=False))

    assert len(top2) == 2, "FAIL: Should return only 2 candidates"
    print("\nRESULT: PASSED ✅")


# ============================================================
# TEST 7: Full Integration Pipeline
# ============================================================
def test_full_pipeline():
    print("\n" + "="*50)
    print("TEST 7: Full Integration Pipeline")
    print("="*50)

    # Simulated job description (as it would come from user input)
    job_description_raw = """
    We are looking for a Python Developer with 2+ years of experience.
    Must have skills in: Machine Learning, Data Science, Pandas, NumPy,
    Scikit-learn, SQL, and REST APIs. Experience with TensorFlow is a plus.
    """

    # Simulated resumes (as they would come after PDF extraction)
    resumes_raw = {
        "Candidate_A": """
        Python developer with 3 years experience. Skilled in Machine Learning,
        Deep Learning, TensorFlow, Pandas, NumPy, Scikit-learn, SQL, REST APIs.
        """,
        "Candidate_B": """
        Java developer experienced in Spring Boot, Hibernate, MySQL, Microservices,
        Docker, Kubernetes, REST APIs, AWS Cloud.
        """,
        "Candidate_C": """
        Data Scientist with Python, Pandas, NumPy, Data Analysis, Machine Learning,
        Statistical Modeling, Scikit-learn, Matplotlib.
        """
    }

    # Step 1: Clean job description
    cleaned_job = clean_text(job_description_raw)

    # Step 2: Clean each resume and calculate similarity
    candidate_scores = {}
    for name, resume_text in resumes_raw.items():
        cleaned_resume = clean_text(resume_text)
        score = calculate_similarity(cleaned_job, cleaned_resume)
        candidate_scores[name] = score
        print(f"  {name}: {score}%")

    # Step 3: Rank candidates
    ranked = rank_candidates(candidate_scores)
    print("\n--- Final Rankings ---")
    print(ranked.to_string(index=False))

    assert not ranked.empty, "FAIL: Rankings should not be empty"
    print("\nRESULT: PASSED ✅")


# ============================================================
# RUN ALL TESTS
# ============================================================
if __name__ == "__main__":
    print("\n" + "="*50)
    print("   AI RESUME SCREENING - INTEGRATION TESTS")
    print("="*50)

    tests = [
        test_clean_text,
        test_empty_text,
        test_high_similarity,
        test_low_similarity,
        test_ranking,
        test_top_candidates,
        test_full_pipeline
    ]

    passed = 0
    failed = 0

    for test in tests:
        try:
            test()
            passed += 1
        except AssertionError as e:
            print(f"\n❌ {e}")
            failed += 1
        except Exception as e:
            print(f"\n❌ Unexpected Error in {test.__name__}: {e}")
            failed += 1

    print("\n" + "="*50)
    print(f"TESTS COMPLETE: {passed} passed ✅ | {failed} failed ❌")
    print("="*50)
