import asyncio


async def hola():
    print("hola.....")
    await asyncio.sleep(5)      # espera que el sleep termine
    print(".....mundo!!!")


if __name__ == "__main__":
    # event loop
    asyncio.run(hola())
