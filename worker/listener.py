from worker import spin_up

import socketio

workers=[]

from threading import Thread
import time
import json



def read_checkpoint():
    try:
        with open('Contents/checkpoint.json', 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        return {"Completed epochs" : 0}
        
def heartbeat():
    while True:
        
        # Call the function to read data from JSON
        data = read_checkpoint()
        # Use the data as needed
        if "Completed epochs" not in data:
            sio.emit('heartbeat',0)
        else:
            sio.emit('heartbeat',data["Completed epochs"])
            time.sleep(10)
        
hb = Thread(target=heartbeat)

import requests

key = "not assigned"

def downloadData(token):
    print(token)
    respdata = requests.get(f"http://172.16.129.26:5000/download/{token}").content
    # print(respdata)
    with open('worker.zip', 'wb') as f:
        f.write(respdata)

sio = socketio.Client()

@sio.event
def connect():
    if hb.is_alive() == False:
        hb.start()
    print("I'm connected!")

@sio.event
def disconnect():
    print("I'm disconnected!")

@sio.on('chunk-upload')
def on_message(token):
    print('I received a message!')
    downloadData(token)
    spin_up(key)

@sio.on('keyEvent')
def on_message(keyr):
    global key
    key = keyr
    print('I received my key!')
    # downloadData(token)
    # spin_up()

try:
    sio.connect('http://172.16.129.26:5000')
    sio.wait()
finally:
    sio.disconnect()


# # spawn function calls here
# wrkr = Thread(target=spin_up)
# wrkr.start()
# workers.append(wrkr)


# for wrkr in workers:
#     wrkr.join()