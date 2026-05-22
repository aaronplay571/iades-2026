import signal
from time import sleep


def nuestro_handler(sig, frame):
    global contador
    contador = 0
    print("sig: ", sig)
    print("Saliendo....")
    op = input("esta seguro que desa salir: Y/N").upper()
    if op == "Y":
        exit(1)


# Registrar un handler para la señal del ctrl-C
signal.signal(signal.SIGINT, nuestro_handler)

contador = 0

while True:
    contador += 1
    print(f"procesando....{contador}")
    sleep(5)
