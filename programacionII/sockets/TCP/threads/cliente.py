"""

| Method      | Description          |
| ----------- | -------------------- |
| `socket()`  | Create socket        | (S - C)
| `bind()`    | Attach to IP + port  | (S)
| `listen()`  | Wait for connections | (S)
| `accept()`  | Accept connection    | (S)
| `connect()` | Connect to server    | (C)
| `send()`    | Send data            | (S/C)
| `recv()`    | Receive data         | (S/C)
| `close()`   | Close connection     | (S / C) -- liberar el socket


"""
import socket


SERVER_IP = "127.0.0.1"
SERVER_PORT = 5002

# Crear el socket TCP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as soc:
    soc.connect((SERVER_IP, SERVER_PORT))

    while True:
        msg = input("IN: ")
        if msg == "fin":
            break
        
        soc.sendall(msg.encode())

        datos = soc.recv(1024)
        print("datos: ", {datos.decode()})



