from dotenv import find_dotenv, load_dotenv

import logging
import os
import socket
import threading

load_dotenv(find_dotenv())


logging.basicConfig(
    # filename='app.log',
    # DEBUG → INFO → WARNING → ERROR → CRITICAL
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)


IP_SERVER = os.getenv("IP_SERVER")
PORT_SERVER = int(os.getenv("PORT_SERVER"))

MAX_PENDING_CON = int(os.getenv("MAX_PENDING_CON"))


def server_function(conn, addr):
    logging.info(f"Cliente: {addr}")
    while True:
        datos = conn.recv(1024).decode()
        if not datos:
            break

        logging.debug(f"(data received: {datos}")
        conn.send(f"echo: {datos}".encode())
    logging.info(f"Closed: {conn}")
    conn.close()


if __name__ == "__main__":
    logging.info("Server starting...")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as conn:
        conn.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        conn.bind((IP_SERVER, PORT_SERVER))
        conn.listen(MAX_PENDING_CON)
        logging.info("Server started!!!")
        while True:
            client_con, addr = conn.accept()
            thread_conn = threading.Thread(target=server_function, args=(client_con, addr))
            thread_conn.daemon = True
            thread_conn.start()
