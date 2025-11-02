# 🧩 The Four Core json Functions in Python
# Function	Purpose	Works With	Common Use
# json.dump()	Write Python data to a JSON file	File object	Save data to a .json file
# json.load()	Read JSON data from a file	File object	Load data back from .json file
# json.dumps()	Convert Python data to a JSON string	String variable	Send JSON data (e.g. to API)
# json.loads()	Convert JSON string back to Python data	String variable	Read JSON string (e.g. from web)

import os
import json

employ = {
    "name": "John Doe",
    "age": 30,
    "city": "New York",
    "skills": ["Python", "JavaScript", "SQL"],
    "projects": {
        "project1": "Web Development"
    }
}

file_path = os.path.dirname(__file__)
correct_path = os.path.join(file_path, "file", "employ.json")

# Make sure the "file" directory exists
os.makedirs(os.path.dirname(correct_path), exist_ok=True)

# Check if the file already exists
if os.path.exists(correct_path):
    with open(correct_path, 'r') as file:
        data = json.load(file)
        print("🟡 JSON file already exists. Here is the current content:\n")
        print(json.dumps(data, indent=4))
else:
    try:
        with open(correct_path, 'w') as file:
            json.dump(employ, file, indent=4)
            print(f"✅ JSON file created at {correct_path}")
    except Exception as e:
        print(f"❌ An error occurred: {e}")
