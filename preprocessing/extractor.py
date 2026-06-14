# ============================================================
# extractor.py - Resume Text Extraction Module
# Programmer 1: Resume Text Extraction & Preprocessing
# ============================================================
# This file reads PDF resume files and extracts raw text
# from them using the PyPDF2 library.
# ============================================================

import PyPDF2  # Library to read PDF files
import os      # To check if file exists


def extract_text(pdf_file):
    """
    Extracts all readable text from a PDF resume file.

    Parameters:
        pdf_file (str or file-like object): Path to the PDF file or a file object.

    Returns:
        str: Extracted raw text from the PDF.
             Returns empty string if file is empty or corrupted.
    """

    extracted_text = ""  # Start with empty text

    try:
        # Open and read the PDF file
        pdf_reader = PyPDF2.PdfReader(pdf_file)

        # Check if PDF has any pages
        if len(pdf_reader.pages) == 0:
            print("Warning: PDF has no pages.")
            return ""

        # Loop through each page and extract text
        for page_number in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_number]  # Get the page
            page_text = page.extract_text()        # Extract text from page

            # Some pages may return None if they have no text
            if page_text:
                extracted_text += page_text + "\n"  # Add page text with newline

    except PyPDF2.errors.PdfReadError:
        # Handle corrupted or unreadable PDF files
        print("Error: Could not read PDF. File may be corrupted.")
        return ""

    except FileNotFoundError:
        # Handle missing files
        print(f"Error: File not found.")
        return ""

    except Exception as e:
        # Catch any other unexpected errors
        print(f"Unexpected error while reading PDF: {e}")
        return ""

    return extracted_text  # Return the full extracted text


# -------------------------------------------------------
# Testing the extractor (only runs if this file is run directly)
# -------------------------------------------------------
if __name__ == "__main__":
    # Test with a sample PDF if available
    test_pdf = "sample_resume.pdf"

    if os.path.exists(test_pdf):
        text = extract_text(test_pdf)
        print("=== Extracted Text ===")
        print(text[:500])  # Print first 500 characters
    else:
        print("No test PDF found. Please provide a sample_resume.pdf to test.")
