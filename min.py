import os
import aiohttp
from bs4 import BeautifulSoup
from telegram import Bot
import asyncio

# Secrets سے لی گئی ویلیوز
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
URL = "https://1waqhg.life/casino/play/spribe_aviator?p=e9g9"

bot = Bot(token=BOT_TOKEN)

async def get_latest_crash():
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(URL) as response:
                html = await response.text()
                soup = BeautifulSoup(html, 'html.parser')
                crash_elements = soup.find_all("div", class_="crash-point")
                if crash_elements:
                    crash = crash_elements[-1].text.strip()
                    return crash
                return "کوئی ڈیٹا نہیں ملا"
    except Exception as e:
        return f"خرابی: {str(e)}"

async def main():
    result = await get_latest_crash()
    await bot.send_message(chat_id=CHAT_ID, text=f"تازہ ترین کریش: {result}")

if __name__ == "__main__":
    asyncio.run(main())
