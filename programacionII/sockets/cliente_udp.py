import socket
import sys

SERVER_IP = "127.0.0.1"
SERVER_PORT = 5001

dato = sys.argv[1]

# Crear el socket UDP
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as soc:
    soc.sendto(dato.encode(), (SERVER_IP, SERVER_PORT))

    datos, _ = soc.recvfrom(1024)
    print(f"datos: ", {datos.decode()})

