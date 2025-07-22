import streamlit as st

# Debug: Confirm app has started
st.write("✅ App loaded successfully")
from resume_parser import extract_text_from_pdf_or_image
from matcher import match_resumes

# Page setup
st.set_page_config(page_title="Smart Resume Screener", layout="wide")
st.title("🔍 Smart Resume Screening Tool")
st.markdown("""
A personalized AI-powered application by **Jigyasha Chouhan** to intelligently match resumes against job descriptions using NLP techniques like TF-IDF and Cosine Similarity.
""")

# --- Customization Parameters ---
THRESHOLD = 0  # Only display resumes with 50% or higher match

# --- Input Fields ---
job_desc = st.text_area("📝 Paste the Job Description:", height=200)

uploaded_files = st.file_uploader("📎 Upload Resume Files (PDF Only)", type=["pdf", "jpeg", "jpg","png","HTML DOC","text"], accept_multiple_files=True)

# --- Resume Matching Logic ---
if st.button("🚀 Match Resumes"):
    st.write("🚀 Match button clicked")
    if not job_desc or not uploaded_files:
        st.warning("⚠️ Please enter a job description and upload at least one resume.")
    else:
        resume_texts = []
        resume_names = []

        # Extract text from uploaded PDFs
        for file in uploaded_files:
            text = extract_text_from_pdf_or_image(file)
            resume_texts.append(text)
            resume_names.append(file.name)

        # Generate similarity scores
        results = match_resumes(job_desc, resume_texts, resume_names)
        results['Match Score'] *=4
        # Filter and display only relevant matches
        filtered_results = results[results['Match Score'] >= THRESHOLD]

        st.subheader("📊 Matching Results")
        st.markdown(f"Displaying resumes with match score **≥ {THRESHOLD}%**")

        if not filtered_results.empty:
            # Add ranking to results
            filtered_results = filtered_results.reset_index(drop=True)
            filtered_results.index = filtered_results.index + 1
            filtered_results.insert(0, "Rank", filtered_results.index)

            # Search/filter box
            search_query = st.text_input("🔍 Search resumes by name:").lower()
            filtered_display = filtered_results[filtered_results['Resume'].str.lower().str.contains(search_query)] if search_query else filtered_results

            # Display ranked table
            st.dataframe(filtered_display, use_container_width=True)

            # Download as CSV
            csv = filtered_display.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="📥 Download Results as CSV",
                data=csv,
                file_name="resume_match_results.csv",
                mime="text/csv"
            )

            # Display each result with progress bar
            for i, row in filtered_results.iterrows():
                resume_name = row["Resume"]
                match_score = row["Match Score"]

                # Show medals for top 3 ranks
                medal = ""
                if i == 0:
                    medal = "🥇"
                elif i == 1:
                    medal = "🥈"
                elif i == 2:
                    medal = "🥉"

                st.write(f"{medal} **{resume_name}**")
                st.progress(int(match_score))
        else:
            st.info("🔎 No resumes met the threshold score. Try lowering the threshold or uploading different resumes.")
