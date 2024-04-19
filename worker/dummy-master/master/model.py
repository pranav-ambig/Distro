import os

print("Hello world!")
# Get the current file's directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the path to the CSV file
csv_file_path = os.path.join(current_dir, "chunk.csv")

# Read the name of the CSV file
with open(csv_file_path, "r") as file:
    csv_file_name = file.name

print("CSV file name:", csv_file_name)