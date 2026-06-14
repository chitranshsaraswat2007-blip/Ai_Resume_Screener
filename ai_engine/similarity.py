# ============================================================
# similarity.py - AI Similarity Scoring Module
# Programmer 2: AI Similarity & Candidate Ranking Module
# ============================================================
# This file compares a resume against a job description
# using TF-IDF vectorization and Cosine Similarity.
#
# What is TF-IDF?
#   TF = Term Frequency  → How often a word appears in a document
#   IDF = Inverse Document Frequency → How rare the word is across documents
#   Together, TF-IDF gives a score to each word showing its importance.
#
# What is Cosine Similarity?
#   It measures the angle between two text vectors.
#   Score of 1.0 = identical, 0.0 = completely different
# ============================================================

from sklearn.feature_extraction.text import TfidfVectorizer  # TF-IDF tool
from sklearn.metrics.pairwise import cosine_similarity        # Cosine similarity tool


def calculate_similarity(job_description, resume_text):
    """
    Calculates how similar a resume is to a job description.

    Uses TF-IDF + Cosine Similarity.

    Parameters:
        job_description (str): Cleaned job description text.
        resume_text (str): Cleaned resume text.

    Returns:
        float: Similarity score between 0.0 and 1.0
               (multiplied by 100 to give a percentage)
    """

    # Safety check - return 0 if either text is empty
    if not job_description or not resume_text:
        return 0.0

    # Step 1: Put both texts into a list for TF-IDF processing
    documents = [job_description, resume_text]

    # Step 2: Create TF-IDF Vectorizer
    # This converts text into numerical vectors (numbers) that the computer understands
    vectorizer = TfidfVectorizer()

    # Step 3: Fit and transform both documents into TF-IDF vectors
    # fit_transform() learns the vocabulary and converts text to numbers
    tfidf_matrix = vectorizer.fit_transform(documents)

    # Step 4: Calculate Cosine Similarity between the two vectors
    # tfidf_matrix[0] = job description vector
    # tfidf_matrix[1] = resume vector
    similarity_score = cosine_similarity(tfidf_matrix[0], tfidf_matrix[1])

    # Step 5: Extract the score and convert to percentage
    # cosine_similarity returns a 2D array, so we get [0][0]
    score_percentage = round(float(similarity_score[0][0]) * 100, 2)

    return score_percentage  # Return as percentage (e.g., 78.45)


# -------------------------------------------------------
# Testing similarity (only runs if this file is run directly)
# -------------------------------------------------------
if __name__ == "__main__":
    job_desc = """
    we are looking for a python developer with experience in machine learning
    data science pandas numpy scikit learn deep learning
    """

    resume1 = """
    python developer skilled in machine learning deep learning
    pandas data analysis scikit learn tensorflow
    """

    resume2 = """
    graphic designer experienced in adobe photoshop illustrator
    ui ux design creative branding logo
    """

    score1 = calculate_similarity(job_desc, resume1)
    score2 = calculate_similarity(job_desc, resume2)

    print(f"Resume 1 (Python Dev) Similarity: {score1}%")
    print(f"Resume 2 (Graphic Designer) Similarity: {score2}%")
