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

Cliente...

1. Se conecta con el servidor

2. El servidor envia una lista con los archivos disponibles en formato json

3. El cliente envia el nombre del archivo que quiere descargar


"""
import json
import socket

SERV_PORT = 5003
SERV_IP = "localhost"


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as conn:

    conn.connect((SERV_IP, SERV_PORT))
    print("Esperando los archivos disponibles....")
    #recibo en datos la lista con los archicos - binario
    archivos_b = conn.recv(1024)
    
    # datos ahora esta en formato json
    archivos_json = archivos_b.decode()
    archivos = json.loads(archivos_json)
    print("Archivos disponibles")

    for indice, archivo in enumerate(archivos):
        print(f"{indice}. {archivo}")

    archivo_indice = int(input("Ingrese el archivo a transferir (indice): "))

    print("archivos: ", archivos)
    print("indice: ", archivo_indice)
    
    conn.sendall(archivos[archivo_indice].encode())

    with open(archivos[archivo_indice], 'wb') as file:
        while True:
            datos = conn.recv(1024)
            print(datos)
            if not datos:
                break
            file.write(datos)

    print(f"Archivo {archivos[archivo_indice]} transferido")

