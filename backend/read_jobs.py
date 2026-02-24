import json

def jobs():
    with open("jobs.json", "r") as file:
        data = json.load(file)

    return data