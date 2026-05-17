"""
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

# localhost 
IP_SERVER = "127.0.0.1"  
PORT_SERVER = 5001


# Crear el socket TCP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as soc:
    # Asociare una direccion IP y un Puerto
    soc.bind((IP_SERVER,PORT_SERVER))
    # ponerlo a escuchar....pedidos de conexion
    soc.listen()

    print(f"Escuchando conexiones en el puerto: {PORT_SERVER}")
    # se queda aca hasta que llega una coexion  - bloqueante
    while(True):
        conn, addr = soc.accept()

        with conn:
            print(f"Se conecto: {addr}")
            while True:
                datos = conn.recv(1024)
                if not datos:
                    break
                print(f"Datos recibidos: ", {datos.decode()})
                # enviamos los datos
                conn.sendall(datos)






