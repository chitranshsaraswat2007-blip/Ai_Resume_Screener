# ============================================================
# app.py - Streamlit Frontend Interface
# Programmer 3: Frontend & User Interface
# ============================================================
# This is the main web application file. Run it with:
#     streamlit run app.py
#
# It provides:
#   - Resume upload (multiple PDFs)
#   - Job description input
#   - Analyze button
#   - Ranked results table
# ============================================================

import streamlit as st      # Streamlit - for building the web UI
import pandas as pd          # For displaying data tables
import sys
import os

# Add project root to path so we can import our modules
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Import our custom modules
from preprocessing.extractor import extract_text
from preprocessing.cleaner import clean_text
from ai_engine.similarity import calculate_similarity
from ai_engine.ranking import rank_candidates


# ============================================================
# PAGE CONFIGURATION
# ============================================================
st.set_page_config(
    page_title="AI Resume Screener",   # Tab title in browser
    page_icon="📄",                    # Tab icon
    layout="wide"                      # Use full width layout
)


# ============================================================
# APP TITLE & DESCRIPTION
# ============================================================
st.title("📄 AI Resume Screening & Candidate Ranking System")
st.markdown("Upload resumes and enter a job description to automatically rank candidates by best fit.")
st.divider()  # Horizontal line separator


# ============================================================
# LAYOUT: Two columns side by side
# ============================================================
col1, col2 = st.columns([1, 1])  # Split page into two equal columns


# ============================================================
# LEFT COLUMN: File Upload
# ============================================================
with col1:
    st.subheader("📁 Upload Resumes")
    st.markdown("Upload one or more PDF resumes below:")

    # File uploader - allows multiple PDF files
    uploaded_files = st.file_uploader(
        label="Choose PDF files",
        type=["pdf"],            # Only allow PDF files
        accept_multiple_files=True  # Allow multiple uploads
    )

    # Show how many files were uploaded
    if uploaded_files:
        st.success(f"✅ {len(uploaded_files)} resume(s) uploaded successfully!")


# ============================================================
# RIGHT COLUMN: Job Description Input
# ============================================================
with col2:
    st.subheader("📝 Job Description")
    st.markdown("Paste the job description you are hiring for:")

    # Large text area for job description
    job_description = st.text_area(
        label="Enter Job Description",
        placeholder="Example: We are looking for a Python developer with experience in machine learning, data science, pandas, numpy, and scikit-learn...",
        height=200  # Height of the text box
    )


st.divider()


# ============================================================
# ANALYZE BUTTON
# ============================================================
analyze_button = st.button("🔍 Analyze Resumes", type="primary", use_container_width=True)


# ============================================================
# PROCESSING & RESULTS
# ============================================================
if analyze_button:

    # --- Validation Checks ---
    if not uploaded_files:
        st.warning("⚠️ Please upload at least one PDF resume.")

    elif not job_description.strip():
        st.warning("⚠️ Please enter a job description.")

    else:
        # Show a loading spinner while processing
        with st.spinner("🤖 Analyzing resumes... Please wait."):

            # Step 1: Clean the job description text
            cleaned_job_desc = clean_text(job_description)

            # Step 2: Process each uploaded resume
            candidate_scores = {}   # Dictionary to store {name: score}
            failed_files = []        # Track any files that failed

            for resume_file in uploaded_files:
                try:
                    # Extract text from the PDF
                    raw_text = extract_text(resume_file)

                    # Clean the extracted text
                    cleaned_resume = clean_text(raw_text)

                    # Calculate similarity score against job description
                    score = calculate_similarity(cleaned_job_desc, cleaned_resume)

                    # Store the score with the filename as the candidate name
                    candidate_name = resume_file.name.replace(".pdf", "").replace("_", " ")
                    candidate_scores[candidate_name] = score

                except Exception as e:
                    # If a file fails, track it
                    failed_files.append(resume_file.name)

            # Step 3: Rank all candidates
            ranked_df = rank_candidates(candidate_scores)

        # ============================================================
        # DISPLAY RESULTS
        # ============================================================
        st.success("✅ Analysis Complete!")
        st.subheader("🏆 Candidate Rankings")

        if not ranked_df.empty:
            # Add a color indicator column based on score
            def score_label(score):
                if score >= 70:
                    return "🟢 Strong Match"
                elif score >= 40:
                    return "🟡 Moderate Match"
                else:
                    return "🔴 Weak Match"

            ranked_df["Match Status"] = ranked_df["Match Score (%)"].apply(score_label)

            # Display the full ranking table
            st.dataframe(
                ranked_df,
                use_container_width=True,   # Full width table
                hide_index=True              # Hide default row index
            )

            # Show top candidate separately
            top_candidate = ranked_df.iloc[0]
            st.info(f"🥇 **Top Candidate:** {top_candidate['Candidate Name']} with a match score of **{top_candidate['Match Score (%)']}%**")

            # Bar chart visualization
            st.subheader("📊 Match Score Chart")
            chart_data = ranked_df.set_index("Candidate Name")["Match Score (%)"]
            st.bar_chart(chart_data)

        else:
            st.error("No results to display. All files may have failed to process.")

        # Show failed files if any
        if failed_files:
            st.warning(f"⚠️ The following files could not be processed: {', '.join(failed_files)}")


# ============================================================
# FOOTER
# ============================================================
st.divider()
st.markdown(
    "<p style='text-align:center; color:gray;'>AI Resume Screening System | Built with Streamlit & Scikit-learn</p>",
    unsafe_allow_html=True
)
