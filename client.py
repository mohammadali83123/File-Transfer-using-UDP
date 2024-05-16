DEST_IP = ""
DEST_PORT = 16666
COMMAND = "lsend"

import socket
import sys
import os
import UDPReceiver
import UDPSender
import logging

# Initialize logger
logging.basicConfig(
    format=
    '%(asctime)s,%(msecs)03d - %(levelname)s - %(funcName)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    level=logging.NOTSET)
logger = logging.getLogger()


def clientMain():
    if COMMAND != "lsend" and COMMAND != "lget":
        logger.info("Unknown command!")
        os._exit(0)
    localFilePath = "C:\\Users\\M ALI\\Downloads\\CN-Project\\Test\\Client\\" + MY_LARGE_FILE

    if COMMAND == "lsend" and os.path.isfile(localFilePath) == False:
        logger.info("File not exist :" + localFilePath)
        os._exit(0)
    else:
        logger.info("The file you have chosen is " + localFilePath)

    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    clientSocket.sendto(
        bytearray("HAND SHAKE 1", "utf-8"), (DEST_IP, DEST_PORT))
    serverData, serverAddr = clientSocket.recvfrom(1024)
    serverData = serverData.decode('utf-8')
    if serverData == "HAND SHAKE 2":
        logger.info("Client receives HAND SHAKE 2")
        clientSocket.sendto(
            bytearray("HAND SHAKE 3", "utf-8"), (DEST_IP, DEST_PORT))
    else:
        logger.info("Connection failed!")
        exit(0)
    logger.info("Connect to the server successfully!")

    serverData, serverAddr = clientSocket.recvfrom(1024)
    serverPort = int(serverData.decode('utf-8'))
    logger.info("Transfer port is " + str(serverPort))

    clientSocket.sendto(bytearray(COMMAND, "utf-8"), (DEST_IP, serverPort))
    serverData, serverAddr = clientSocket.recvfrom(1024)
    serverData = serverData.decode('utf-8')
    logger.info("Server replies: " + serverData)
    
    clientSocket.sendto(
        bytearray(MY_LARGE_FILE, "utf-8"), (DEST_IP, serverPort))
    serverData, serverAddr = clientSocket.recvfrom(1024)
    serverData = serverData.decode('utf-8')
    logger.info("Server replies: " + serverData)
    if serverData == "File not exist":
        return

    # Transfer file
    if COMMAND == "lsend":
        logger.info("Send " + localFilePath + " to " + str(serverAddr))
        UDPSender.sendFile(serverAddr, localFilePath)
    else:
        logger.info("Receive " + localFilePath + " to " + str(serverAddr))
        UDPReceiver.getFile(serverPort, localFilePath)


if __name__ == "__main__":
    COMMAND = sys.argv[1]
    DEST_IP, DEST_PORT = sys.argv[2].split(':')
    DEST_PORT = int(DEST_PORT)
    MY_LARGE_FILE = sys.argv[3]
    clientMain()