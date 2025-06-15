# Reliable UDP File Transfer with Congestion and Flow Control

This project implements a reliable file transfer system using UDP, incorporating key features of TCP such as congestion control, flow control, and packet sequencing.

## 📦 Components

### 1. Client

The client initiates communication and handles commands to **send (`lsend`)** or **receive (`lget`)** files from the server.

#### Supported Operations:

- **Send a file to server:**

```bash
python client.py lsend <server_ip:server_port> <file_path>
```

- **Receive a file from server:**

```bash
python client.py lget <server_ip:server_port> <file_name>
```

### 2. Server

The server listens on a specified port for client connections and processes file transfer commands.

#### Start the server:

```bash
python server.py
```

By default, the server listens on port **20000**.

---

## 🔁 File Transfer Process

1. **Connection Initialization:**  
   The client establishes a logical connection to the server (simulated TCP handshake).

2. **Command Exchange:**  
   Client sends either `lsend` or `lget` command.

3. **File Transfer:**  
   - `lsend`: Client sends a file to the server.  
   - `lget`: Server sends a file to the client.

---

## ⚙️ Configuration

You can configure the following parameters inside the code:

| Parameter        | Description                                      |
|------------------|--------------------------------------------------|
| `DEST_IP`        | IP address of the server                         |
| `DEST_PORT`      | Port number of the server                        |
| `COMMAND`        | Command to execute (`lsend` or `lget`)           |
| `MY_LARGE_FILE`  | File path for the file to transfer (for `lsend`) |

---

## 📡 Network Protocol

This system is built over UDP sockets and includes the following reliability features:

### ✅ Reliability Features

- **Packet Sequencing** to reassemble data in correct order.
- **Acknowledgements (ACKs)** to confirm delivery.
- **Timeouts & Retransmissions** for lost packets.
- **Sliding Window Protocol** for flow control.
- **Congestion Control**:
  - Adjusts window size dynamically based on ACKs/timeouts.
  - Implements a simple congestion avoidance mechanism.

---

## 📋 Dependencies

- Python 3.x
- Standard Python libraries:
  - `socket`
  - `threading`
  - `logging`
  - `os`, `sys`, etc.

No external packages required.

---

## 📁 Directory Structure

```plaintext
.
├── client.py        # Client-side script to send/receive files
├── server.py        # Server-side script to listen and respond
├── utils/           # (Optional) Contains helper modules (e.g., packet.py)
├── README.md        # Project documentation
```

---

## 🧪 Usage Example

1. **Start the server (on Terminal 1):**

```bash
python server.py
```

2. **Send file from client (on Terminal 2):**

```bash
python client.py lsend 127.0.0.1:20000 myfile.txt
```

3. **Receive file from server:**

```bash
python client.py lget 127.0.0.1:20000 myfile.txt
```

---

## 🛠 Future Improvements

- Add encryption for secure transfers
- Implement Selective Acknowledgements (SACK)
- Add checksums for data integrity
- Add a GUI for ease of use

---

## 📑 License

This project is open source and available under the [MIT License](LICENSE).

---

## 🙋‍♂️ Author

Developed by [Your Name]  
Feel free to contribute, open issues, or submit pull requests!
