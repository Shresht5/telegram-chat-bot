from aiogram import Router,types,filters,html
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from utils.aiogram_functions.messages import reference

#  aiogram router
router = Router()


#  This handler receives messages with `/help` command
@router.message(filters.Command('start'))
async def command_start_handler(message: types.Message):

    await message.reply(f"Hi.\n    I am an AI-powered Telegram chat bot created by Shreshta.\n- Built in 2026 using Python.\n- Designed to answer questions, explain concepts, and assist with everyday queries.\n- Supports commands like /start, /help, /clear, and normal chat messages.\n- You can ask me anything—I respond like an AI assistant to help you think, learn, and solve problems.\n\n try - \"best 5 healthcare tips\"")

#  This handler receives messages with `/help` command
@router.message(filters.Command('help'))
async def command_handler(message: types.Message):

    await message.reply("Hi there, I'm AI assistent created by Shreshta!\nfor make your life easier \n /start - to start the conversation \n /help - to get this help menu\n /clear - clear previous chat\n- if you write anything other tan this so it will treat as asking qiostion as ai chat")

#  This handler receives messages with `/clear` command
@router.message(filters.Command('clear'))
async def command_handler(message: types.Message):
    reference.clear()
    await message.reply("previous chat is removed in server")

