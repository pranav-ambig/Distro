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




import json
def write_checkpoint(epno ):
    
    with open("Contents/checkpoint.json", 'w+') as file:
        json.dump({"Completed epochs" : epno}, file)


def rename_chunks(directory="Contents/", prefix="chunk", extension=".csv"):

  for filename in os.listdir(directory):
    match = re.search(rf"{prefix}(\d+){extension}", filename)
    if match:
      old_file_path = os.path.join(directory, filename)
      new_number = match.group(1)  # Extract the captured number
      new_file_name = (directory + f"{prefix}{extension}")
      
  
      os.rename(old_file_path, new_file_name)

import os

import time
def create_worker_instance():

    subprocess.run(["docker",  "image", "build", "-t", "worker1", "."])

    # Run the docker command
    subprocess.run(["docker", "run" , "-e", f"worker_key={key}", "worker1"])
    time.sleep(10)
    subprocess.run(["docker", "cp" , "worker1:/Contents/checkpoint.json" , "."])

global key  
  
def spin_up(keyr):
    key = keyr
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
    
