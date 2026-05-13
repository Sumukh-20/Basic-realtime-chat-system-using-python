import socket
import threading

# --- Configuration ---
# 127.0.0.1 is the "localhost" IP address. It means "this computer".
HOST = '0.0.0.0' 
# The port number is like a door number. Let's use 5555. 
# (Make sure it's over 1024 to avoid system reserved ports)
PORT = 5555        

# Create the server socket
# AF_INET means we are using IPv4 addresses. 
# SOCK_STREAM means we are using TCP (reliable delivery).
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

# Lists to keep track of connected clients and their names
clients = []
nicknames = []

def broadcast(message):
    """Sends a message to all connected clients."""
    for client in clients:
        try:
            client.send(message)
        except:
            # If sending fails, the client probably disconnected. We'll handle cleanup later.
            pass

def handle_client(client):
    """Handles an individual client connection continuously."""
    while True:
        try:
            # Wait to receive a message from the client (max 1024 bytes)
            message = client.recv(1024)
            # Broadcast the message to everyone
            broadcast(message)
        except:
            # If there's an error (e.g., client closed the window), remove them
            index = clients.index(client)
            clients.remove(client)
            client.close()
            
            # Announce that they left
            nickname = nicknames[index]
            broadcast(f"{nickname} left the chat!".encode('utf-8'))
            nicknames.remove(nickname)
            break

def receive_connections():
    """Main loop to listen for new people joining the chat."""
    print("Server is up and running. Waiting for connections...")
    
    while True:
        # Accept a new connection
        client, address = server.accept()
        print(f"Connected with {str(address)}")
        
        # Ask the client for their nickname
        # We send a secret code word 'NICK' to trigger the client to send their name
        client.send("NICK".encode('utf-8'))
        nickname = client.recv(1024).decode('utf-8')
        
        # Add the new client and their nickname to our lists
        nicknames.append(nickname)
        clients.append(client)
        
        print(f"Nickname of the client is {nickname}!")
        broadcast(f"{nickname} joined the chat!".encode('utf-8'))
        client.send("Connected to the server!".encode('utf-8'))
        
        # Start a new thread to handle this specific client
        # We use threads so the server can handle multiple clients at the same time
        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()

# Start the server
if __name__ == "__main__":
    receive_connections()