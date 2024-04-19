import zipfile
import subprocess
import os
import re
import shutil

def extract_zip_file(zip_file_path, extract_path):
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(extract_path)

# Example usage
zip_file_path = 'worker.zip'
extract_path = 'Contents/'


def rename_chunks(directory="Contents/", prefix="chunk", extension=".csv"):

  for filename in os.listdir(directory):
    match = re.search(rf"{prefix}(\d+){extension}", filename)
    if match:
      old_file_path = os.path.join(directory, filename)
      new_number = match.group(1)  # Extract the captured number
      new_file_name = (directory + f"{prefix}{extension}")
      
  
      os.rename(old_file_path, new_file_name)

def create_worker_instance():

    subprocess.run(["docker",  "image", "build", "-t", "worker1", "."])
    subprocess.run(["docker", "run", "worker1"])
    
def spin_up():
    # Check if the folder exists
    if os.path.exists("Contents/"):
      # Delete the folder and its contents
      shutil.rmtree("Contents/")
      
    extract_zip_file(zip_file_path, extract_path)
    print("done extracting")
    rename_chunks()
    print("done renaming")
    create_worker_instance()
    print("done creating worker instance")
    
