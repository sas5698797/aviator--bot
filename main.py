import os
import aiohttp
from bs4 import BeautifulSoup
from telegram import Bot

BOT_TOKEN = "8199514053:AAHulhyWB92HiqaHwJmDQnaPWTBTHh5qSfI"
CHAT_ID = "7427054317"
URL = "https://1waqhg.life/casino/play/spribe_aviator?p=e9g9"

bot = Bot(token=BOT_TOKEN)

async def get_latest_crash():
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(URL) as response:
                html = await response.text()
                soup = BeautifulSoup(html, 'html.parser')
                crash = soup.find_all("div", class_="crash-point")[-1].text
                return crash
    except Exception as e:
        return f"Error: {e}"

async def main():
    result = await get_latest_crash()
    await bot.send_message(chat_id=CHAT_ID, text=f"Crash: {result}")

import asyncio
asyncio.run(main())
