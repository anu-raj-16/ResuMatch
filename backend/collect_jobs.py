import json

jobs = [
    {
        "company": "Microsoft",
        "role": "Software Developer",
        "description": "work on cloud",
        "location": "Toronto",
        "education": "Computer Science Degree",
        "experience": "5 years",
        "skills": ["Azure"]
    },
    {
        "company": "Amazon",
        "role": "Software Engineer",
        "description": "",
        "location": "Vancouver",
        "education": "Software Engineering Degree",
        "experience": "0-3 years",
        "skills": ["Python", "Java", "OOP"]
    },
]

with open("jobs.json", "w", newline = "") as file:
    json.dump(jobs, file, indent = 2)