import zipfile
import subprocess

def extract_zip_file(zip_file_path, extract_path):
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(extract_path)

# Example usage
zip_file_path = 'master.zip'
extract_path = 'Contents/'
# Contents contains job.py chunks.zip
extract_zip_file(zip_file_path, extract_path)


def create_worker_instance():

    subprocess.run(["docker",  "image", "build", "-t", "worker1", "."])
    subprocess.run(["docker", "run", "worker1"])
    

create_worker_instance()