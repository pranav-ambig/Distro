

from worker import spin_up

import socketio

workers=[]

from threading import Thread


import base64


def decodeData(data):
    # print(data)
    bindata = base64.b64decode(data)
    with open('worker.zip', 'wb') as f:
        f.write(bindata)

sio = socketio.Client()

@sio.event
def connect():
    print("I'm connected!")

@sio.event
def disconnect():
    print("I'm disconnected!")

@sio.on('chunk-upload')
def on_message(data):
    print('I received a message!')
    decodeData(data)
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
    
    
