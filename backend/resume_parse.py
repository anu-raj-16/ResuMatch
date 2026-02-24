import os
import re

def read_resume(path):
    with open(path, "r") as file:
        text = file.read()
        return text.lower()
    

def extract_skills(text):
    known_skills = [
        "python",
        "java",
        "sql",
        "backend",
        "frontend",
        "react",
        "azure",
        "aws"
    ]

    found_skills = [

    ]

    for skill in known_skills:
        if skill in text:
            found_skills.append(skill)
    
    return found_skills

def extract_education(text):
    if "computer science" in text:
        return "Computer Science Degree"
    elif "software engineering" in text:
        return "Software Engineering Degree"
    elif "engineering" in text:
        return "Engineering Degree"
    else:
        return None

def extract_experience(text):
    exp = re.search(r"(\d+)\s*years?", text)
    if exp:
        return int(exp.group(1))
    
    return None

def parse_resume(p):
    BASE_DIR = os.path.dirname(__file__)
    resume_path = os.path.join(BASE_DIR, p)

    t = read_resume(resume_path)

    resume = {
        "education": extract_education(t),
        "experience": extract_experience(t),
        "skills": extract_skills(t)
    }

    return resume




