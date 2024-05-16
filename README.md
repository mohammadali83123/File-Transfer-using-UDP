Building a Reliable UDP(with Congestion control and Flow Control)


The system consists of two main components:

Client: Initiates file transfers by sending commands to a server.
Server: Listens for client connections and handles file transfer requests.

Prerequisites
Python 3.x installed.
Basic understanding of networking and Python programming.

Components
Client
The client is responsible for initiating file transfers by sending commands (lsend or lget) to a specified server.

Operations:
To send a file:
$ python client.py lsend <server_ip:server_port> <file_path>

To receive a file:
$ python client.py lget <server_ip:server_port> <file_name>

Server
The server listens for incoming connections from clients and manages file transfer requests.

Usage
Start the server:
$ python server.py
The server listens on a specified port (default: 20000) for incoming connections.

File Transfer Process
TCP Handshake: Establishes a connection between the client and server.
Command Exchange: Client sends a command (lsend or lget) to the server.
File Transfer:
For lsend: Client sends a large file to the server.
For lget: Server sends a requested file to the client.


Configuration
You can configure the following parameters:

DEST_IP: Destination IP address of the server.
DEST_PORT: Destination port of the server.
COMMAND: Command (lsend or lget).
MY_LARGE_FILE: Path to the large file you want to transfer.

Dependencies
The project uses Python's built-in socket library for network communication.

Implementation Details
UDP Sender/Receiver: Implements reliable file transfer over UDP, inspired by TCP's behavior.
Logging: Utilizes Python's logging module for detailed event logging.
Congestion Control: Implements a basic form of congestion control to manage packet flow.

Usage
Start the server on the host machine:

$ python server.py
Run the client on a different machine or as a separate process:

$ python client.py <operation> <127.0.0.1:2000> <file_path>
