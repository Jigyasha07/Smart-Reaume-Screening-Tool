from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

def match_resumes(job_description, resume_texts, resume_names):
    documents = [job_description] + resume_texts
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(documents)

    job_vec = tfidf_matrix[0]
    resume_vecs = tfidf_matrix[1:]

    scores = cosine_similarity(job_vec, resume_vecs)[0] * 100
    results = pd.DataFrame({
        'Resume': resume_names,
        'Match Score': scores.round(2)
    }).sort_values(by='Match Score', ascending=False).reset_index(drop=True)
    return results
