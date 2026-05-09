import threading

# Variable global
contador = 0


# Tarea de cada hilo
def incrementador(nombre):
    global contador

    for _ in range(100):
        contador += 1
    
    print(f"termino: {nombre}")


# definimos dos hilos
hilo1 = threading.Thread(target=incrementador, args=("hilo 1",))
hilo2 = threading.Thread(target=incrementador, args=("hilo 2",))

# Iniciamo los hilos
hilo1.start()
hilo2.start()

hilo1.join()
hilo2.join()

print(f"el valor del contador es: {contador}")

