# Use the official Python base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /

# Copy the requirements file to the container
COPY Contents/ .

# Install the Python dependencies
RUN pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
RUN pip install -r requirements.txt

# Set environment variables
# ENV worker_key=value1 

# Set the command to run when the container starts
ENTRYPOINT [ "python", "model.py" , "echo ${worker_key}"]