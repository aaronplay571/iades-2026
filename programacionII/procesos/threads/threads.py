import threading
import time

# simular las distintas tareas de cada thread
def tarea(nombre, tiempo):
    print(f"Comenzando tarea: {nombre}")
    time.sleep(tiempo)
    print(f"Terminando tarea: {nombre}")


hilo1 = threading.Thread(target=tarea, args=("Tarea1", 30))
hilo2 = threading.Thread(target=tarea, args=("Tarea2", 40))


hilo1.start()
hilo2.start()


hilo1.join()
hilo2.join()


print("Las dos tareas terminaron!!!")













