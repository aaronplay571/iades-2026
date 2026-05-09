import asyncio

from datetime import datetime


async def tarea(nombre, segundos):
    print(f"Tarea: {nombre} comenzo")
    print("inicio: ", datetime.now())
    await asyncio.sleep(segundos)
    print(f"Tarea: {nombre} termino")
    print("fin: ", datetime.now())
    return f"{nombre} -- {segundos}"


async def main():
    resultados = await asyncio.gather(
        tarea("Tarea 1", 30),
        tarea("Tarea 2", 20),
        tarea("Tarea 3", 50)
    )
    print("resultados: ", resultados)


# event loop
asyncio.run(main())