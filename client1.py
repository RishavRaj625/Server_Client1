import socket

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
# SERVER = "192.168.61.1"
SERVER = "192.168.29.149"
ADDR = (SERVER,PORT)

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    
    print(client.recv(2048).decode(FORMAT)) # receiving the message from server

send("Hello Lapi!")
input() # input enter it give the message received 
send("Hello My Dear Friend!")
input()
send("I got 7lpa package in TCS!")

send(DISCONNECT_MESSAGE)
