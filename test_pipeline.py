

import os
from preprocessing.extractor import extract_text
from preprocessing.cleaner import clean_text
from ai_engine.similarity import calculate_similarity
from ai_engine.ranking import rank_candidates

def run_test_scenario(jd_title, jd_text, resumes_dir):
    print("=" * 60)
    print(f"RUNNING SCENARIO: {jd_title}")
    print("=" * 60)
    
    # 1. Clean the Job Description
    cleaned_jd = clean_text(jd_text)
    print(f"Cleaned JD length: {len(cleaned_jd)} characters")
    
    # 2. Get all resumes in the directory
    resume_files = [f for f in os.listdir(resumes_dir) if f.endswith(".pdf")]
    
    candidate_scores = {}
    invalid_files = []
    
    # 3. Process each resume
    for filename in resume_files:
        filepath = os.path.join(resumes_dir, filename)
        print(f"\nProcessing '{filename}'...")
        
        # 3.1 Extract text
        raw_text = extract_text(filepath)
        if not raw_text.strip():
            print(f"--> Warning: Extraction returned empty text (corrupted/blank).")
            invalid_files.append(filename)
            candidate_scores[filename] = 0.0
            continue
            
        # 3.2 Clean text
        cleaned_text = clean_text(raw_text)
        if not cleaned_text.strip():
            print(f"--> Warning: Cleaner returned empty text.")
            invalid_files.append(filename)
            candidate_scores[filename] = 0.0
            continue
            
        # 3.3 Compute Similarity score
        score = calculate_similarity(cleaned_jd, cleaned_text)
        print(f"--> Raw Similarity Score: {score:.4f} ({score * 100:.2f}%)")
        candidate_scores[filename] = score

    # 4. Rank candidates
    ranked_df = rank_candidates(candidate_scores)
    
    print("\n" + "-" * 40)
    print("FINAL RANKING TABLE:")
    print("-" * 40)
    print(ranked_df.to_string(index=False))
    
    if invalid_files:
        print("\nInvalid / Corrupted files detected:")
        for inv in invalid_files:
            print(f" - {inv} (Scored 0.00%)")
            
    print("\n")

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    resumes_dir = os.path.join(base_dir, "sample_resumes")
    
    # Verify the sample_resumes folder exists
    if not os.path.exists(resumes_dir):
        print(f"Error: {resumes_dir} directory not found. Please run create_samples.py first.")
        return
        
    # SCENARIO 1: Python Developer job description
    python_jd = (
        "We are looking for a Python Developer to join our backend team. "
        "The candidate must have experience in Python, web frameworks such as Django or Flask, "
        "databases like PostgreSQL, and building RESTful APIs. Knowledge of git and Docker is highly preferred."
    )
    run_test_scenario("Python Backend Developer", python_jd, resumes_dir)
    
    # SCENARIO 2: Data Scientist job description
    ds_jd = (
        "Looking for a Data Scientist to build machine learning models. "
        "Requirements: expertise in Python, SQL, statistical analysis, and packages like "
        "Pandas, NumPy, Scikit-learn. PyTorch or TensorFlow experience is a plus."
    )
    run_test_scenario("Data Scientist", ds_jd, resumes_dir)

if __name__ == "__main__":
    main()
