import resume_parse as resume_parse
import read_jobs as read_jobs

resume = resume_parse.parse_resume("resume.txt")
jobs = read_jobs.jobs()

matches = []

for job in jobs:
    match = 0
    if job["education"] == resume["education"]:
        match += 33
    if job["experience"] <= resume["experience"]:
        match += 33

    sm = 0
    for skill in job["skills"]:
        if skill.lower() in resume["skills"]:
            print("true")
            sm += 1
    
    sm = int(sm/len(job["skills"])*100)
    match += sm
    
    matches.append({
        "company": job["company"],
        "role": job["role"],
        "score": match
    })

print(matches)