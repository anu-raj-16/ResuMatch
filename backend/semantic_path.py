from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from read_jobs import jobs as get_jobs
import json

with open('backend/resume.txt', 'r') as file: # dont use absolute addresses like this
    content = file.read()

# print(content)

jobs = get_jobs()
# print(jobs)

matches = []

for job in jobs:
    document = [content, job["education"], job["description"], job["role"]]

    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(document)
    similarity_matrix = cosine_similarity(tfidf_matrix, tfidf_matrix)

    matches.append(
        {"company": job["company"],
        "job role": job["role"],
        "role match": f"{similarity_matrix[0][3]:.2%}",
        "education required": job["education"],
        "education match": f"{similarity_matrix[0][1]:.2%}",
        "job description match": f"{similarity_matrix[0][2]:.2%}"
        }
    )

print(matches)