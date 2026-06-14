# ============================================================
# ranking.py - Candidate Ranking Module
# Programmer 2: AI Similarity & Candidate Ranking Module
# ============================================================
# This file takes similarity scores for all candidates
# and ranks them from best match to lowest match.
# ============================================================

import pandas as pd  # Pandas is used to create nice tables (DataFrames)


def rank_candidates(candidate_scores):
    """
    Ranks candidates based on their similarity scores.

    Parameters:
        candidate_scores (dict): A dictionary where:
            - key   = candidate name (str)
            - value = similarity score (float, percentage)

        Example:
            {
                "Alice_Resume.pdf": 85.5,
                "Bob_Resume.pdf": 62.3,
                "Charlie_Resume.pdf": 91.0
            }

    Returns:
        pandas.DataFrame: A ranked table with columns:
            - Rank
            - Candidate Name
            - Match Score (%)
    """

    # Safety check - return empty DataFrame if no data
    if not candidate_scores:
        print("Warning: No candidate scores provided.")
        return pd.DataFrame()

    # Step 1: Convert dictionary to a Pandas DataFrame
    # This creates a 2-column table: Candidate Name | Match Score (%)
    df = pd.DataFrame(
        list(candidate_scores.items()),
        columns=["Candidate Name", "Match Score (%)"]
    )

    # Step 2: Sort candidates from highest score to lowest score
    # ascending=False means highest first
    df = df.sort_values(by="Match Score (%)", ascending=False)

    # Step 3: Reset index so row numbers are clean (0, 1, 2...)
    df = df.reset_index(drop=True)

    # Step 4: Add a Rank column (1st, 2nd, 3rd...)
    df.insert(0, "Rank", range(1, len(df) + 1))

    return df  # Return ranked table


def get_top_candidates(candidate_scores, top_n=3):
    """
    Returns the top N ranked candidates.

    Parameters:
        candidate_scores (dict): Dictionary of candidate names and scores.
        top_n (int): Number of top candidates to return. Default is 3.

    Returns:
        pandas.DataFrame: Top N candidates ranked.
    """
    ranked_df = rank_candidates(candidate_scores)

    # Return only top N rows
    return ranked_df.head(top_n)


# -------------------------------------------------------
# Testing ranking (only runs if this file is run directly)
# -------------------------------------------------------
if __name__ == "__main__":
    # Sample candidate scores
    sample_scores = {
        "Alice_Resume.pdf": 85.5,
        "Bob_Resume.pdf": 62.3,
        "Charlie_Resume.pdf": 91.0,
        "Diana_Resume.pdf": 47.8,
        "Eve_Resume.pdf": 78.2
    }

    print("=== Full Candidate Rankings ===")
    ranked = rank_candidates(sample_scores)
    print(ranked.to_string(index=False))

    print("\n=== Top 3 Candidates ===")
    top3 = get_top_candidates(sample_scores, top_n=3)
    print(top3.to_string(index=False))
