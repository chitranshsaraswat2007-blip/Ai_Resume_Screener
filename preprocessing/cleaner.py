
import re

def clean_text(text):
    """
    Cleans raw text by:
    1. Converting to lowercase.
    2. Removing numbers, punctuation, and special characters.
    3. Collapsing multiple whitespaces into a single space and stripping edges.
    
    Parameters:
        text (str): The raw input text.
        
    Returns:
        str: The preprocessed/cleaned text.
    """
    if not text or not isinstance(text, str):
        return ""
    
    # Step 1: Convert text to lowercase
    cleaned = text.lower()
    
    # Step 2: Remove numbers, punctuation, and special symbols
    # We use a regular expression to keep only alphabetical characters (a-z) and spaces.
    # [^a-z\s] matches any character that is NOT a lowercase letter or a whitespace character.
    # We replace them with a space to prevent joining words accidentally (e.g. "python3" -> "python ").
    cleaned = re.sub(r'[^a-z\s]', ' ', cleaned)
    
    # Step 3: Remove extra spaces, tabs, and newlines
    # \s+ matches one or more whitespace characters. We replace them with a single space.
    cleaned = re.sub(r'\s+', ' ', cleaned)
    
    # Step 4: Remove leading and trailing spaces
    cleaned = cleaned.strip()
    
    return cleaned

# Self-testing block
if __name__ == "__main__":
    test_input = "Hello!!! This is a sample resume for Python Developer (Role 123). Contact: dev@example.com."
    print("Testing cleaner.py...")
    print(f"Input:  '{test_input}'")
    print(f"Output: '{clean_text(test_input)}'")
