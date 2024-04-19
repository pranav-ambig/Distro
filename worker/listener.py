import socket

from worker import spin_up

# Define the IP address and port number for the worker node
worker_ip = 'http://172.16.129.26'
worker_port = 5000

# Create a socket object
worker_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the IP address and port number
worker_socket.bind((worker_ip, worker_port))

# Listen for incoming connections
worker_socket.listen()

print(f"Worker node is listening on {worker_ip}:{worker_port}")


workers=[]

from threading import Thread

while True:
    # Accept a connection from the orchestrator
    orchestrator_socket, orchestrator_address = worker_socket.accept()
    print(f"Connected to orchestrator at {orchestrator_address}")

    # Receive data from the orchestrator
    data = orchestrator_socket.recv(1024).decode()
    print(f"Received message from orchestrator: {data}")

    # spawn function calls here
    wrkr = Thread(target=spin_up)
    wrkr.start()
    workers.append(wrkr)
    
    # Process the received data

    # Send a response back to the orchestrator
    response = "Message received"
    orchestrator_socket.send(response.encode())

    # Close the connection with the orchestrator
    orchestrator_socket.close()
    break

for wrkr in workers:
    wrkr.join()
    
    
