import socket
import threading

HEADER = 64
PORT = 5050
# SERVER = "192.165.24.141"  # we can also add the specific IP addresses or any public IP addresses

SERVER = socket.gethostbyname(socket.gethostname()) # local/ laptop local host IP address

print(socket.gethostname())
print(SERVER)

ADDR = (SERVER,PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn,addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            
            if msg == DISCONNECT_MESSAGE:
                connected = False  # or break
                
            print(f"[{addr}] {msg}")
            # Sending message back to client
            conn.send("Msg received..".encode(FORMAT))
            
            
    conn.close()    

def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn,addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")
        
print("[STARTING] server is starting....")
start()
