# 💬 Real-Time Python Chat System

This is a real-time, multi-client chat application built using Python's built-in `socket` and `threading` libraries. It uses a Client-Server architecture to broadcast messages across a Local Area Network (LAN).

This project was built as a Project-Based Learning (PBL) submission to demonstrate core networking and concurrency concepts in Python.

## 🚀 Features
* **Multi-client support:** Multiple users can connect to the server simultaneously.
* **Real-time broadcasting:** Messages sent by one client are instantly broadcasted to all other connected clients.
* **Concurrency:** The server uses the `threading` module to handle each client connection independently without blocking the main execution.
* **Custom Nicknames:** Users can choose their own display names upon joining.
* **Join/Leave Notifications:** The chat room announces when users connect or disconnect.

## 🛠️ Technologies Used
* **Python 3.x**
* `socket` (Networking/TCP connections)
* `threading` (Handling concurrent client connections)

## 💻 How to Run the Project

### Prerequisites
Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).

### 1. Start the Server
The server must be running before any clients can connect. Open your terminal or command prompt and run:
```bash
python server.py
