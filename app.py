import streamlit as st
import pandas as pd
import io

# Import project modules
from preprocessing.extractor import extract_text
from preprocessing.cleaner import clean_text
from ai_engine.similarity import calculate_similarity
from ai_engine.ranking import rank_candidates

# Set up Streamlit Page configuration
st.set_page_config(
    page_title="AI Resume Screening & Ranking System",
    page_icon="📄",
    layout="wide"
)

# Page header
st.title("📄 AI Resume Screening & Candidate Ranking System")
st.markdown("""
Welcome to the AI Resume Screener! Upload candidate resumes in PDF format, 
provide the Job Description (JD), and find the best matching candidates in seconds.
""")

# Setup grid layout: Left panel for input, Right panel for results
col1, col2 = st.columns([1, 1.2], gap="large")

with col1:
    st.subheader("📋 Input Section")
    
    # 1. Job Description text area
    job_description = st.text_area(
        label="Enter Job Description:",
        placeholder="Paste the target job description here (e.g. skills, experience, technologies required)...",
        height=250,
        help="Provide details about the job, including core languages, libraries, databases, and general experience requirements."
    )
    
    # 2. File uploader for resumes (multiple PDFs)
    uploaded_files = st.file_uploader(
        label="Upload Resumes (PDF format only):",
        type=["pdf"],
        accept_multiple_files=True,
        help="You can drag and drop multiple PDF resume files here."
    )
    
    # 3. Analyze button
    analyze_button = st.button(
        label="🚀 Analyze & Rank Candidates",
        type="primary",
        use_container_width=True
    )

with col2:
    st.subheader("🏆 Candidate Ranking Results")
    
    if analyze_button:
        # Input Validation
        if not job_description.strip():
            st.error("⚠️ Please enter a Job Description before running the analysis.")
        elif not uploaded_files:
            st.error("⚠️ Please upload at least one PDF resume file before running the analysis.")
        else:
            # Process Job Description
            cleaned_jd = clean_text(job_description)
            
            if not cleaned_jd:
                st.error("⚠️ The provided Job Description does not contain any valid text for comparison after cleaning.")
            else:
                candidate_scores = {}
                invalid_files = []
                
                # Show loading spinner
                with st.spinner("Extracting text and calculating similarity scores..."):
                    for uploaded_file in uploaded_files:
                        file_name = uploaded_file.name
                        
                        # Read file bytes into a buffer so PyPDF2 can parse it
                        file_buffer = io.BytesIO(uploaded_file.read())
                        
                        # Extract text
                        raw_text = extract_text(file_buffer)
                        
                        # Handle empty or corrupted files
                        if not raw_text.strip():
                            # Record as invalid and assign 0.0 score
                            invalid_files.append(file_name)
                            candidate_scores[file_name] = 0.0
                            continue
                            
                        # Clean text
                        cleaned_resume = clean_text(raw_text)
                        
                        if not cleaned_resume.strip():
                            invalid_files.append(file_name + " (no readable text)")
                            candidate_scores[file_name] = 0.0
                            continue
                            
                        # Calculate Cosine Similarity
                        score = calculate_similarity(cleaned_jd, cleaned_resume)
                        candidate_scores[file_name] = score
                
                # Rank candidates
                ranked_df = rank_candidates(candidate_scores)
                
                # Display Results
                st.success("✅ Analysis completed successfully!")
                
                if not ranked_df.empty:
                    # Highlight top match
                    top_candidate = ranked_df.iloc[0]
                    if top_candidate['Similarity Score'] > 0.0:
                        st.balloons()
                        st.info(f"💡 **Top Candidate:** **{top_candidate['Candidate Name']}** with a match of **{top_candidate['Match Percentage']}**!")
                    
                    # Display the ranking table
                    st.dataframe(
                        ranked_df,
                        use_container_width=True,
                        hide_index=True
                    )
                    
                    # Optional download link for the table
                    csv = ranked_df.to_csv(index=False).encode('utf-8')
                    st.download_button(
                        label="📥 Download Rankings as CSV",
                        data=csv,
                        file_name="candidate_rankings.csv",
                        mime="text/csv"
                    )
                else:
                    st.warning("No candidate scores could be determined.")
                
                # Display warnings about corrupted/empty files
                if invalid_files:
                    st.warning(
                        "⚠️ **The following files were empty, corrupted, or contained no readable text:**\n" + 
                        "\n".join([f"- {name}" for name in invalid_files]) +
                        "\n\n*Note: These files were scored 0.0% and ranked at the bottom.*"
                    )
    else:
        # Default screen before analysis
        st.info("Upload resumes on the left, paste the job description, and click 'Analyze & Rank Candidates' to view results.")
