import asyncio

from datetime import datetime


async def tarea(nombre, segundos):
    print(f"Tarea: {nombre} comenzo")
    print("inicio: ", datetime.now())
    await asyncio.sleep(segundos)
    print(f"Tarea: {nombre} termino")
    print("fin: ", datetime.now())


async def main():
    t1 = asyncio.create_task(tarea("Tarea 1", 60))
    t2 = asyncio.create_task(tarea("Tarea 2", 60))

    print("Esperando tareas....")
    await t1
    await t2

    print("tareas finalizadas....")


# event loop
asyncio.run(main())
