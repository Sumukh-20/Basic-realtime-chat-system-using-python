import socket
import threading

# Ask the user for a name before connecting
nickname = input("Choose a nickname: ")

# --- Configuration ---
# Must match the server's IP and port!
HOST = '192.168.9.225'
PORT = 5555

# Create the client socket and connect to the server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

def receive_messages():
    """Constantly listens for messages coming from the server."""
    while True:
        try:
            # Receive data from the server
            message = client.recv(1024).decode('utf-8')
            
            # If the server asks for the nickname, send it
            if message == 'NICK':
                client.send(nickname.encode('utf-8'))
            else:
                # Otherwise, it's a normal chat message, so print it to the screen
                print(message)
        except Exception as e:
            # If an error occurs, close the connection and exit
            print("An error occurred. Disconnected from server.")
            client.close()
            break

def write_messages():
    """Constantly waits for the user to type something and sends it."""
    while True:
        try:
            # Get input from the user
            user_input = input("")
            # Format it as "Nickname: Message"
            message = f"{nickname}: {user_input}"
            # Send it to the server
            client.send(message.encode('utf-8'))
        except:
            print("Error sending message.")
            client.close()
            break

# Start the listening thread
receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

# Start the writing loop (this runs on the main thread)
write_messages()