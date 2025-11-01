import os

# Get the folder where THIS script (test.py) lives
base_dir = os.path.dirname(__file__)

# Build a path to file/test.txt inside that same folder
file_path = os.path.join(base_dir, "file", "test.txt")

print("Checking file path:", file_path)

if os.path.exists(file_path):
    print(f"The file {file_path} exists ✅")

    if os.path.isfile(file_path):
        print(f"{file_path} is a file.")

        with open(file_path, 'r') as file:
            content = file.read()
            print("File content:")
            print(content)
    elif os.path.isdir(file_path):
        print(f"{file_path} is a directory.")
    else:
        print(f"{file_path} is neither a file nor a directory.")
else:
    print(f"The file {file_path} does not exist ❌")
