import os
import logging
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
import sys
import asyncio
from utils.aiogram_functions.command_messages import router as router1
from utils.aiogram_functions.messages import router as router2

# Load Env variable
load_dotenv()
TELEGRAM_BOT_TOKEN=os.getenv("TELEGRAM_BOT_TOKEN")

# configure logging
logging.basicConfig(level=logging.INFO)

# initialize bot and dispatch
bot=Bot(token=TELEGRAM_BOT_TOKEN)
dp=Dispatcher()

# router 
dp.include_router(router1)
dp.include_router(router2)

async def main():
    await dp.start_polling(bot)

# start server
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())