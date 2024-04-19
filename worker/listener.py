

from worker import spin_up

import socketio

workers=[]

from threading import Thread


import base64

def decodeData(data):
    bindata = base64.b64decode(data[0])
    with open('worker.zip', 'wb') as f:
        f.write(bindata)
    

# standard Python
with socketio.SimpleClient() as sio:
    # ... connect to a server and use the client
    # ... no need to manually disconnect!
    sio.connect('http://172.16.129.26:5000')
    event = sio.receive()
    print(f'received event: "{event[0]}" with arguments {event[1:]}')
    decodeData(event[1:])



# spawn function calls here
wrkr = Thread(target=spin_up)
wrkr.start()
workers.append(wrkr)


for wrkr in workers:
    wrkr.join()
    
    
