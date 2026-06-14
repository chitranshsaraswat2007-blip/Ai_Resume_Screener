from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def calculate_similarity(job_description, resume):
    """
    Calculates the TF-IDF Cosine Similarity score between a job description and a resume.
    
    Parameters:
        job_description (str): Preprocessed text of the job description.
        resume (str): Preprocessed text of the resume.
        
    Returns:
        float: Similarity score between 0.0 and 1.0. Returns 0.0 if either input is empty or error occurs.
    """
    # Guard against empty input text
    if not job_description.strip() or not resume.strip():
        return 0.0
        
    try:
        # Initialize Scikit-learn's TF-IDF Vectorizer
        # We specify stop_words='english' to ignore common grammatical words (and, the, with, in, etc.)
        # which increases matching accuracy for skill keywords.
        vectorizer = TfidfVectorizer(stop_words='english')
        
        # Fit the vectorizer on both texts and transform them into TF-IDF matrices (vectors)
        # This aligns the features (words) so that both vectors have the same dimensions.
        tfidf_matrix = vectorizer.fit_transform([job_description, resume])
        
        # Compute Cosine Similarity between the first vector (job description) 
        # and the second vector (resume).
        # tfidf_matrix[0:1] gets the first row as a 2D matrix (needed by cosine_similarity)
        # tfidf_matrix[1:2] gets the second row as a 2D matrix
        similarity_matrix = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])
        
        # The result is a 2D array, we extract the single float value at index [0][0]
        score = similarity_matrix[0][0]
        
        return float(score)
        
    except ValueError as e:
        # Handle cases where the text contains only non-word characters or has no vocabulary
        print(f"Warning: TF-IDF vectorizer failed (likely due to empty vocabulary after processing): {e}")
        return 0.0
    except Exception as e:
        print(f"Error calculating similarity: {e}")
        return 0.0

# Self-testing block
if __name__ == "__main__":
    print("Testing similarity.py...")
    jd = "python developer machine learning data science"
    resume_1 = "python developer with experience in machine learning and data science"
    resume_2 = "java developer web design database sql"
    
    score_1 = calculate_similarity(jd, resume_1)
    score_2 = calculate_similarity(jd, resume_2)
    
    print(f"JD vs Resume 1 similarity: {score_1:.4f} ({score_1*100:.2f}%)")
    print(f"JD vs Resume 2 similarity: {score_2:.4f} ({score_2*100:.2f}%)")
