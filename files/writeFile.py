import os

# Text to write
text_data = "I like pizza"

# Get current script directory
file_path = os.path.dirname(__file__)

# Join path to the "file" folder and "output.txt"
correct_path = os.path.join(file_path, "file", "output.txt")

try:
    # Try to create a new file ('x' mode)
    with open(correct_path, 'x') as file:
        file.write(text_data)
        print(f"✅ Data written to {correct_path}, creating output.txt")

except FileExistsError:
    # If file already exists, append text
    with open(correct_path, 'a') as file:
        file.write("\n" + text_data)  # <-- FIXED: use + to combine strings
        print(f"🟡 Data appended to {correct_path}, output.txt already exists")
