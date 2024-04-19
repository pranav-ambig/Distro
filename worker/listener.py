from worker import spin_up

import socketio

workers=[]

from threading import Thread
import time
def heartbeat():
    while True:
        sio.emit('heartbeat',"I'm alive")
        time.sleep(10)
        
hb = Thread(target=heartbeat)

import requests

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
    spin_up()

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