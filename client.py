import socket
from hmac1 import generate_hmac

SERVER_IP = "127.0.0.1"  # Replace with the server's IP in GNS3
SERVER_PORT = 5000
BUFFER_SIZE = 1024

def send_file(file_name, server_ip, server_port):
    key = b"my_secret_key"  # Shared secret key
    with open(file_name, "rb") as f:
        file_data = f.read()

    # Generate HMAC for the file
    hmac_value = generate_hmac(key, file_data.decode())

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((server_ip, server_port))

        # Send file name
        client_socket.send(file_name.encode())
        print(client_socket.recv(BUFFER_SIZE).decode())

        # Send HMAC
        client_socket.send(hmac_value.encode())
        print(client_socket.recv(BUFFER_SIZE).decode())

        # Send file data
        client_socket.send(file_data)
        print(client_socket.recv(BUFFER_SIZE).decode())

        # Get server response
        server_response = client_socket.recv(BUFFER_SIZE).decode()
        print(f"Server response: {server_response}")

if __name__ == "__main__":
    # Example file
    file_name = "example_file.txt"
    with open(file_name, "w") as f:
        f.write("This is a test file for HMAC verification.")

    send_file(file_name, SERVER_IP, SERVER_PORT)
