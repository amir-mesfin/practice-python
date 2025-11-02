import os
import json
import csv

# Folder path
file_path = os.path.join(os.path.dirname(__file__), "file")

# File paths
text_path = os.path.join(file_path, "employ.txt")
json_path = os.path.join(file_path, "employ.json")
csv_path = os.path.join(file_path, "employees.csv")

# Make sure "file" folder exists
os.makedirs(file_path, exist_ok=True)

# Function to read text file
def read_text_file():
    if not os.path.exists(text_path):
        print(f"❌ Text file not found at {text_path}")
        return
    try:
            with open(text_path, 'r') as file:
                content = file.read().strip()
                print("📄 Text File Content:\n")
                print(content if content else "(File is empty)")
    except Exception as e:
             print(f"❌ An error occurred while reading the text file: {e}")

# Function to read json file
def read_json_file():
    if not os.path.exists(json_path):
        print(f"❌ JSON file not found at {json_path}")
        return
    try:
        with open(json_pathm, 'r') as file:
            data = json.load(file)
            print("📄 JSON File Content:\n")
            print(json.dumps(data, intend = 6))
    except Exception as e:
        print(f"❌ An error occurred while reading the JSON file: {e}")
# Run function


read_text_file()
read_json_file()
