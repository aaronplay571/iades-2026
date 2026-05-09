import asyncio
import aiohttp


urls = []


async def fetch(session, url):

    async with session.get(url) as response:
        return await response.text()
    

async def main():
    async with aiohttp.ClinetSession() as session:
        