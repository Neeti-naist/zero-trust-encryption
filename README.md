# zero-trust-encryption
Python encryption for Zero-Trust-Project(HMAC implementation)
## overview
In a zero trust model, every request is verified before granting access. This project implements HMAC(Hash-based message authentication code)
to ensure integrity and authenticity of communications in a zero trust environment.

## Installation Requirements

* Python 3.7 or higher

* Libraries: socket, os, hmac, hashlib

 Then, clone the repository and install dependencies:
git clone https://github.com/Neeti-naist/zero-trust-hmac.git
cd zero-trust-hmac
pip install -r requirements.txt

## project structure
.
|-- encryption.py           # Contains HMAC generation and verification logic
|-- client.py               # Client-side implementation for sending files
|-- server.py               # Server-side implementation for receiving and verifying files
|-- test_hmac.py            # Unit tests for HMAC functions
|-- README.md               # Project documentation

## Usage
* Start the server
python server.py

**Run the client
python client.py


## Example of hmac authentication  flow
* The client generates an HMAC signature for a message using a shared secret key.
* The server verifies the HMAC before processing the request.
* If HMAC is valid, the request is accepted; otherwise, its rejected.

## Configuration

## Code Explanation

* HMAC Logic (encryption.py)

This module contains functions to generate and verify HMACs.

generate_hmac(key: bytes, message: str) -> str

Generates an HMAC for a given message using a secret key.

Input:

key: The secret key (in bytes).

message: The input message (in string).

Output:

HMAC in hexadecimal format

Example
hmac_value = generate_hmac(b"my_secret_key", "Hello World")
* verify_hmac(key: bytes, message: str, received_hmac: str) -> bool

Verifies the integrity of a message by comparing a generated HMAC with a received HMAC.
Input:

key: The secret key (in bytes).

message: The original message (in string).

received_hmac: The HMAC received for comparison.

Output:

Returns True if the HMAC matches; otherwise, False.
Example:
is_valid = verify_hmac(b"my_secret_key", "Hello World", hmac_value)

## Client (client.py)

The client program reads a file, generates its HMAC, and sends the file and HMAC to the server.

Key Functions

1. send_file(file_name, server_ip, server_port)

Sends a file and its HMAC to the server.

Steps:

Reads the file content.

Generates the HMAC for the file.

Connects to the server using a TCP socket.

Sends the file name, HMAC, and file content to the server.

Receives the server's response.
Example:
send_file("example.txt", "127.0.0.1", 5000)
2. Execution Flow

Creates a test file named neeti_file.txt.

Calls send_file to transfer the file to the server
## Server (server.py)

The server receives files and their HMACs, verifies their integrity, and stores valid files.

Key Functions

1. start_server()

Listens for incoming connections.

Receives the file name, HMAC, and file content from the client.

Verifies the file's integrity using the provided HMAC.

Stores the file if its integrity is valid; otherwise, discards it.

Sends a response to the client indicating the result.

Example:
start_server()
2. Execution Flow

Creates a directory named cloud_storage to store received files.

Listens on 0.0.0.0:5000 for incoming connections.

## Unit Tests (test_hmac.py)

This module contains unit tests for the HMAC functions using the unittest framework.

Key Tests

test_generate_hmac()

Verifies that the generated HMAC is a valid hexadecimal string.

test_verify_hmac_valid()

Ensures the verify_hmac function returns True for matching HMACs.

test_verify_hmac_invalid()

Ensures the verify_hmac function returns False for non-matching HMACs.


## Example output
1. client output
Filename received
HMAC received
File received
Server response: Integrity verified
2. Server output
Server listening on 0.0.0.0:5000...
Connection established with ('127.0.0.1', 12345)
File example.txt received. Verifying integrity...
Integrity verified for example.txt

## Future Enhancements
Add encryption for file data during transmission.

Implement support for larger file transfers.

Extend the project to handle multiple clients simultaneously.

## Contributing
* fork the repo
* create new branch(git checkout -b feature-name)
* commit your changes(git commit -m "Added feature")
* push to github(git push origin feature-name)
* create pull request


