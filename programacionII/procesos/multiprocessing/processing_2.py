import multiprocessing
import time
import os


def tarea(nombre, tiempo):
    print(f"[{nombre}] -- PID: {os.getpid()} -- PPID: {os.getppid()}")
    time.sleep(tiempo)
    print(f"termino la tarea: {nombre}")


if __name__ == "__main__":
    # Creamos los procesos
    print(f"[PADRE] -- PID: {os.getpid()} -- PPID: {os.getppid()}")
    proceso1 = multiprocessing.Process(target=tarea, args=("Tarea process 1", 10))
    proceso2 = multiprocessing.Process(target=tarea, args=("Tarea process 2", 10))


    # Iniciamos los procesos
    proceso1.start()
    proceso2.start()

    # Esperamos que terminen
    proceso1.join()
    proceso2.join()

    print("Terminamos las tareas!!!")