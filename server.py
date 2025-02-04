import socket
import os
from hmac1 import verify_hmac

SERVER_IP = "0.0.0.0"
SERVER_PORT = 5000
BUFFER_SIZE = 1024
STORAGE_DIR = "cloud_storage"

# Ensure storage directory exists
os.makedirs(STORAGE_DIR, exist_ok=True)

def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((SERVER_IP, SERVER_PORT))
        server_socket.listen(5)
        print(f"Server listening on {SERVER_IP}:{SERVER_PORT}...")

        while True:
            client_socket, client_address = server_socket.accept()
            print(f"Connection established with {client_address}")

            with client_socket:
                # Receive file and HMAC 
                file_name = client_socket.recv(BUFFER_SIZE).decode()
                client_socket.send(b"Filename received")

                hmac_value = client_socket.recv(BUFFER_SIZE).decode()
                client_socket.send(b"HMAC received")

                file_data = client_socket.recv(BUFFER_SIZE)
                client_socket.send(b"File received")

                # Save file and validate
                file_path = os.path.join(STORAGE_DIR, file_name)
                with open(file_path, "wb") as f:
                    f.write(file_data)

                print(f"File {file_name} received. Verifying integrity...")

                # Verify HMAC
                key = b"my_secret_key"  # Ensure this key is shared securely
                if verify_hmac(key, file_data.decode(), hmac_value):
                    print(f"Integrity verified for {file_name}")
                    client_socket.send(b"Integrity verified")
                else:
                    print(f"Integrity failed for {file_name}")
                    os.remove(file_path)  # Remove invalid file
                    client_socket.send(b"Integrity failed")

if __name__ == "__main__":
    start_server()
