# write a flask server with logging level set to error and cors enabled on all urls

from flask import Flask, request, send_file
from flask_cors import CORS
from flask_socketio import SocketIO
import logging
import os
import zipfile
import base64
# import requests

app = Flask(__name__)
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*")

# set logging
logging.basicConfig(level=logging.ERROR)

# Constants
TEMP_DIR = './temp'


# Global Variables
workers = set()

@app.route('/')
def hello_world():
    return 'Hello, World!'

@socketio.on('connect')
def handle_connect():
    workers.add(request.sid)
    print(len(workers), "Workers connected")

@socketio.on('heartbeat')
def handle_hb(msg):
    print(f"Heartbeat from {request.sid}:{msg}")

@socketio.on('disconnect')
def handle_connect():
    workers.remove(request.sid)
    print(len(workers), "Workers connected")

@app.route('/download/<filename>', methods=['GET'])
def serveWorkerZips(filename):
    return send_file(f'./temp/{filename}.zip', as_attachment=True)

@app.route('/upload-zip', methods=['POST'])
def upload_zip():
    # check if the post request has the file part
    if 'file' not in request.files:
        return 'No file part', 400

    file = request.files['file']

    # if user does not select file, browser also
    # submit an empty part without filename
    if file.filename == '':
        return 'No selected file', 400

    if file and file.filename.endswith('.zip'):
        # save the file to a directory
        file.save(os.path.join(TEMP_DIR, file.filename))
        
        with zipfile.ZipFile(os.path.join(TEMP_DIR, file.filename), 'r') as zip_ref:
            zip_ref.extractall(os.path.join(TEMP_DIR, file.filename[:-4]))


        working_folder = os.path.join(TEMP_DIR, file.filename[:-4])

        chunks = []
        for filename in os.listdir(working_folder+'/data'):
                chunks.append(filename)

        for worker, chunk in zip(workers, chunks):
            with zipfile.ZipFile(os.path.join(TEMP_DIR, worker+'.zip'), 'w') as worker_zip:
                worker_zip.write(working_folder+'/model.py', arcname='model.py')
                worker_zip.write(working_folder+'/requirements.txt', arcname='requirements.txt')
                worker_zip.write(working_folder+'/data/'+chunk, arcname='/data/'+chunk)

            socketio.emit('chunk-upload', worker, room=list(workers))
        
        return 'Upload zip successful', 200

    return 'Invalid file type', 400


@app.route('/upload', methods=['GET'])
def handle_upload():
    # Assuming you have some data to send to a worker
    data_to_send = {'message': 'Your data here'}

    # Select a worker from the array
    if workers:
        worker_sid = workers[0]  # For example, you can choose the first worker
        # Emit a custom event to the selected worker
        socketio.emit('upload_data', data_to_send, room=worker_sid)
        return "Data sent to worker"
    else:
        return "No workers available"

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0')
