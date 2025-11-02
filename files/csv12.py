import os
import csv

employees = [
    ["name", "age", "city"],
    ["John", 30, "New York"],
    ["Alice", 25, "London"],
    ["Bob", 35, "Paris"]
]

file_path = os.path.dirname(__file__)
correct_path = os.path.join(file_path, "file", "employees.csv")

# Make sure directory exists
os.makedirs(os.path.dirname(correct_path), exist_ok=True)

try:
    with open(correct_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(employees)  # ✅ write all rows at once
        print(f"✅ CSV file created at {correct_path}")
except Exception as e:
    print(f"❌ An error occurred: {e}")
