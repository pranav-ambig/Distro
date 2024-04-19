# Use the official Python base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the container
COPY Contents/ .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set the command to run when the container starts
CMD [ "python", "model.py" ]