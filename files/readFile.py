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
        with open(json_path, 'r') as file:  # Fixed: changed 'json_pathm' to 'json_path'
            data = json.load(file)
            print("📄 JSON File Content:\n")
            print(json.dumps(data, indent=4))  # Fixed: changed 'intend' to 'indent'
    except Exception as e:
        print(f"❌ An error occurred while reading the JSON file: {e}")

def  read_csv_file():
    if not os.path.exists(csv_path):
        print(f"❌ CSV file not found at {csv_path}")
        return
    try:
        with open(csv_path, 'r') as file:
            reader = csv.reader(file)
            print("📄 CSV File Content:\n")
            for row in reader:
                print(', '.join(row))
    except Exception as e:
        print(f"❌ An error occurred while reading the CSV file: {e}")

# Run functions
read_text_file()
read_json_file()
read_csv_file()
