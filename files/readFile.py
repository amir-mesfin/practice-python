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

    with open(text_path, 'r') as file:
        content = file.read().strip()
        print("📄 Text File Content:\n")
        print(content if content else "(File is empty)")

# Run function
read_text_file()
