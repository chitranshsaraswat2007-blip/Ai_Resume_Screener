# ============================================================
# cleaner.py - Text Cleaning & Preprocessing Module
# Programmer 1: Resume Text Extraction & Preprocessing
# ============================================================
# This file cleans and preprocesses raw resume text
# so it is ready for NLP/AI analysis.
# ============================================================

import re  # Regular expressions for text cleaning


def clean_text(text):
    """
    Cleans and preprocesses raw text extracted from a resume.

    Steps:
        1. Convert text to lowercase
        2. Remove punctuation
        3. Remove numbers
        4. Remove special symbols
        5. Remove extra spaces

    Parameters:
        text (str): Raw text extracted from a PDF resume.

    Returns:
        str: Cleaned and preprocessed text.
    """

    # --- Safety Check ---
    # If text is empty or None, return empty string
    if not text or text.strip() == "":
        print("Warning: Empty text received for cleaning.")
        return ""

    # Step 1: Convert all characters to lowercase
    # This ensures "Python" and "python" are treated the same
    text = text.lower()

    # Step 2: Remove punctuation marks like . , ! ? ; : etc.
    # [^\w\s] means "remove anything that is NOT a word character or space"
    text = re.sub(r'[^\w\s]', '', text)

    # Step 3: Remove numbers (digits 0-9)
    # \d matches any digit
    text = re.sub(r'\d+', '', text)

    # Step 4: Remove special symbols like @, #, $, %, &, etc.
    # \W matches any non-word character
    text = re.sub(r'[^a-z\s]', '', text)

    # Step 5: Remove extra whitespace
    # \s+ matches one or more spaces, tabs, or newlines
    # Replace them all with a single space
    text = re.sub(r'\s+', ' ', text)

    # Strip leading and trailing spaces from the final text
    text = text.strip()

    return text  # Return the cleaned text


def preprocess_resume(raw_text):
    """
    Full preprocessing pipeline for a resume.
    Calls clean_text and returns ready-to-use text.

    Parameters:
        raw_text (str): Raw text from PDF extraction.

    Returns:
        str: Fully cleaned text ready for AI analysis.
    """
    cleaned = clean_text(raw_text)
    return cleaned


# -------------------------------------------------------
# Testing the cleaner (only runs if this file is run directly)
# -------------------------------------------------------
if __name__ == "__main__":
    # Sample raw text to test cleaning
    sample_text = """
    John Doe - Software Engineer!
    Email: john.doe@email.com | Phone: +91-9876543210
    Skills: Python 3.9, Machine Learning, Data Science & Analysis
    Experience: 3 Years @ TechCorp Pvt. Ltd.
    GPA: 8.5/10 (2020-2024)
    """

    print("=== Original Text ===")
    print(sample_text)

    cleaned = clean_text(sample_text)

    print("\n=== Cleaned Text ===")
    print(cleaned)
