"""
1. Listar archivos
2. transferir

Servidor TCP

| Method      | Description          |
| ----------- | -------------------- |
| `socket()`  | Create socket        |
| `bind()`    | Attach to IP + port  |
| `listen()`  | Wait for connections |
| `accept()`  | Accept connection    |
| `connect()` | Connect to server    |
| `send()`    | Send data            |
| `recv()`    | Receive data         |
| `close()`   | Close connection     |

"""


import socket


filename = "archivo1.txt"


SERV_PORT = 5000
SERV_IP = "localhost"


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as conn:

    conn.connect((SERV_IP, SERV_PORT))
    conn.sendall(filename.encode())

    with open(filename, 'wb') as file:
        while True:
            datos = conn.recv(1024)
            if not datos:
                break
            file.write(datos)

print(f"Archivo {filename} transferido")

