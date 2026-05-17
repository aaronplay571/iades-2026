"""
SERVIDOR UDP

| Method      | Description          |
| ----------- | -------------------- |
| `socket()`  | Create socket        | (S)
| `bind()`    | Attach to IP + port  | (S)
| `listen()`  | Wait for connections | (S)
| `accept()`  | Accept connection    |  -
| `connect()` | Connect to server    |  -
| `send()`    | Send data            |  (S)
| `recv()`    | Receive data         |  (S)
| `close()`   | Close connection     |  (S)


"""
import socket


IP_SERVER = "127.0.0.1"  
PORT_SERVER = 5001



with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as soc:
    soc.bind((IP_SERVER,PORT_SERVER))

    # while True:
    # bloqueante
    datos, addr = soc.recvfrom(1024)

    print("Datos recibidos: ", datos.decode())

    soc.sendto(datos, addr)




