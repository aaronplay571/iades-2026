import multiprocessing

contador = 0

def incrementador(nombre):
    global contador

    print("proceso: ", nombre)
    for _ in range(100):
        contador += 1
    print(f"proceso: {nombre}  -- contador: {contador}")    


if __name__ == "__main__":
    # Creamos los procesos
    proceso1 = multiprocessing.Process(target=incrementador, args=("Tarea process 1",))
    proceso2 = multiprocessing.Process(target=incrementador, args=("Tarea process 2",))


    # Iniciamos los procesos
    proceso1.start()
    proceso2.start()

    # Esperamos que terminen
    proceso1.join()
    proceso2.join()

    print("Terminamos las tareas!!!")

    print("contador: ", contador)



    