import os

employ = ["eugene", "alice", "bob", "david", "carol", "patrick", "spongebob"]

# Get the directory of the current script
file_path = os.path.dirname(__file__)

# Create a "file" folder path and "employ.txt" inside it
correct_path = os.path.join(file_path, "file", "employ.txt")

# Ensure the directory exists
os.makedirs(os.path.dirname(correct_path), exist_ok=True)

try:
    # Try writing (this will overwrite if file exists)
    with open(correct_path, 'w') as file:
        for name in employ:
            file.write(name + "\n")
    print(f"✅ Data written to {correct_path}, creating employ.txt")

except FileExistsError:
    # If file exists, append instead
    with open(correct_path, 'a') as file:
        for name in employ:
            file.write(name + "\n")
    print(f"🟡 Data appended to {correct_path}, employ.txt already exists")

finally:
    # Read and display content
    with open(correct_path, 'r') as file:
        content = file.read()
        print("\nFile content:\n")
        print(content)
