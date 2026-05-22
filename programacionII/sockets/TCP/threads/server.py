import socket
import threading

IP_SERVER = "localhost"
PORT_SERVER = 5002

MAX_PENDING_CON = 10


def server_function(conn, addr):
    print(f"Cliente: ", addr)
    while True:
        try:
            datos = conn.recv(1024).decode()
            print("data received: ", datos)
            conn.send(f"echo: {datos}".encode())
        except:
            break
    conn.close()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as conn:
    conn.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    conn.bind((IP_SERVER, PORT_SERVER))
    conn.listen(MAX_PENDING_CON)

    while True:
        client_con, addr = conn.accept()
        thread_conn = threading.Thread(target=server_function, args=(client_con, addr)) 
        thread_conn.daemon = True
        thread_conn.start()
