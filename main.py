import os
import logging
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher,types,filters,html
import requests
import sys
import asyncio
import httpx

class Reference:
    def __init__(self):
        self.response=""

reference=Reference()
# Load Env variable
load_dotenv()
TELEGRAM_BOT_TOKEN=os.getenv("TELEGRAM_BOT_TOKEN")
LLM_API_KEY=os.getenv("LLM_API_KEY")

# Function to format AI text for Telegram
def format_for_telegram(ai_text: str) -> str:
    lines = ai_text.splitlines()
    formatted_lines = []
    for line in lines:
        line = line.strip()
        if line.startswith("1.") or line.startswith("2.") or line.startswith("3."):
            formatted_lines.append(f"<b>{line}</b>")  # bold section headings
        elif line.startswith("- "):
            formatted_lines.append(f"• {line[2:]}")  # bullets
        elif line.startswith("✅"):
            formatted_lines.append(line)  # keep emojis
        else:
            formatted_lines.append(line)
    return "\n".join(formatted_lines)



# configure logging
logging.basicConfig(level=logging.INFO)

# initialize bot and dispatch
bot=Bot(token=TELEGRAM_BOT_TOKEN)
dp=Dispatcher()

#messages start
@dp.message(filters.Command('start'))
async def command_start_handler(message: types.Message):
    """
    This handler receives messages with `/start` command
    """
    await message.reply(f"Hello, \n sir! \n meow")

# message help
@dp.message(filters.Command('help'))
async def command_handler(message: types.Message):
    await message.reply("Hi there, I'm AI assistent created by Shreshta!\nfor make your life easier \n /start -to start the conversation \n/help - to get this help menu")


# chat Ai bot
@dp.message()
async def AI_chat_bot(message: types.Message) -> None:
    """
    Ai assistent reply your message
    """
    try:
        async with httpx.AsyncClient(timeout=20) as client:
            response= await client.post("https://openrouter.ai/api/v1/chat/completions",
                json={
                "model": "deepseek/deepseek-r1-0528:free",
                "messages": [
                    {"role": "system", "content":"You are a concise AI assistant. Reply directly and briefly. Add extra points only if necessary. Avoid long explanations. No more than 1000 charachters",},
                    {"role": "assistant", "content": reference.response},
                    {"role": "user", "content": message.text}
                    ],
                },
                headers={
                "Authorization": f"Bearer {LLM_API_KEY}",
                },
            )
            data=response.json()
            await message.reply(data["choices"][0]["message"]["content"])
            reference.response=data["choices"][0]["message"]["content"]
    except Exception as e:
        await message.answer(f"Error: {e}")
    
async def main():
    await dp.start_polling(bot)

# start server
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())