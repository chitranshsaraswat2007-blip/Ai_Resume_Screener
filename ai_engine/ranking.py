

import pandas as pd

def rank_candidates(candidate_scores):
    """
    Ranks candidates based on their similarity scores in descending order.
    
    Parameters:
        candidate_scores (dict): A dictionary where keys are candidate names (e.g. file names)
                                 and values are similarity scores (floats between 0.0 and 1.0).
                                 Example: {'John_Doe.pdf': 0.825, 'Jane_Smith.pdf': 0.412}
                                 
    Returns:
        pd.DataFrame: A Pandas DataFrame containing columns:
                      - Rank (int)
                      - Candidate Name (str)
                      - Similarity Score (float)
                      - Match Percentage (str, e.g. "82.50%")
    """
    # Guard against empty input
    if not candidate_scores:
        return pd.DataFrame(columns=['Rank', 'Candidate Name', 'Similarity Score', 'Match Percentage'])
        
    # Convert dictionary to list of tuples for processing
    data = []
    for candidate, score in candidate_scores.items():
        # Match percentage is similarity score multiplied by 100
        match_percentage = score * 100
        data.append({
            'Candidate Name': candidate,
            'Similarity Score': round(score, 4),
            'Match Percentage': f"{match_percentage:.2f}%",
            '_score_sort': score # Hidden column for sorting
        })
        
    # Create Pandas DataFrame
    df = pd.DataFrame(data)
    
    # Sort DataFrame by similarity score in descending order
    df = df.sort_values(by='_score_sort', ascending=False)
    
    # Drop the sorting column
    df = df.drop(columns=['_score_sort'])
    
    # Reset index and add Rank column starting from 1
    df = df.reset_index(drop=True)
    df.insert(0, 'Rank', df.index + 1)
    
    return df

# Self-testing block
if __name__ == "__main__":
    print("Testing ranking.py...")
    test_scores = {
        'Alice_Python_CV.pdf': 0.7654,
        'Bob_Java_CV.pdf': 0.2311,
        'Charlie_Data_Scientist.pdf': 0.8943
    }
    ranked_df = rank_candidates(test_scores)
    print("\nRanked Candidates DataFrame:")
    print(ranked_df.to_string(index=False))
