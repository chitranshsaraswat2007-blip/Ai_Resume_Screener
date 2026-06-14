

import PyPDF2
import os
import io

def extract_text(pdf_file):
    """
    Extracts all readable text from a PDF resume.
    
    Parameters:
        pdf_file: Can be a file-like object (e.g., BytesIO from Streamlit uploader) 
                  or a string representing the file path.
                  
    Returns:
        str: Extracted raw text from the PDF. Returns an empty string if the file is
             empty, corrupted, or cannot be read.
    """
    text = ""
    try:
        # Check if the input is a file path string and check if it exists and is empty
        if isinstance(pdf_file, str):
            if not os.path.exists(pdf_file):
                print(f"Error: File path '{pdf_file}' does not exist.")
                return ""
            if os.path.getsize(pdf_file) == 0:
                print(f"Warning: File '{pdf_file}' is empty (0 bytes).")
                return ""
            
            # Open file in binary read mode
            with open(pdf_file, "rb") as f:
                reader = PyPDF2.PdfReader(f)
                text = _read_pages(reader)
        else:
            # Assume it is a file-like object (e.g., uploaded via Streamlit)
            # Check size if possible
            pdf_file.seek(0, io.SEEK_END)
            size = pdf_file.tell()
            pdf_file.seek(0) # Reset pointer
            
            if size == 0:
                print("Warning: Uploaded file is empty (0 bytes).")
                return ""
                
            reader = PyPDF2.PdfReader(pdf_file)
            text = _read_pages(reader)
            
    except PyPDF2.errors.PdfReadError as e:
        print(f"PDF Read Error (possibly corrupted PDF): {e}")
        return ""
    except Exception as e:
        print(f"An unexpected error occurred during PDF text extraction: {e}")
        return ""
        
    return text

def _read_pages(reader):
    """
    Helper function to iterate over PDF pages and extract text.
    """
    full_text = []
    num_pages = len(reader.pages)
    if num_pages == 0:
        print("Warning: PDF contains no pages.")
        return ""
        
    for page_num in range(num_pages):
        page = reader.pages[page_num]
        page_text = page.extract_text()
        if page_text:
            full_text.append(page_text)
            
    return "\n".join(full_text)

# Self-testing block
if __name__ == "__main__":
    # This block allows testing extractor.py directly
    print("Testing extractor.py...")
    # Test with non-existent file
    test_text = extract_text("non_existent_file.pdf")
    print(f"Result for non-existent file: '{test_text}' (Expected: '')")
