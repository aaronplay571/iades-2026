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

MAX_PENDINDING_CONN = 5 

FILES_PATH = "/home/pablo/files"

SERVER_PORT = 5000
SERVER_IP = "0.0.0.0"

# creamos el socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as conn:

    conn.bind((SERVER_IP, SERVER_PORT))
    conn.listen(MAX_PENDINDING_CONN)

    print(f"Server file escuchando en el puerto {SERVER_PORT}")

    while True:

        client_conn, addr = conn.accept()

        print(f"Se conecto: {addr}")

        nombre_archivo = client_conn.recv(1024).decode()

        print("Buscando archivo: ", nombre_archivo)

        archivo = f"{FILES_PATH}/{nombre_archivo}"

        with open(archivo, "rb") as file:

            while True:
                datos = file.read(1024)
                if not datos:
                    break
                client_conn.sendall(datos)

        client_conn.close()



