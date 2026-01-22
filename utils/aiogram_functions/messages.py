from aiogram import Router,types,filters,html
from dotenv import load_dotenv
import os
import httpx
from utils.formating.telegram_api_formating import markdowwn_to_html_format
router=Router()

class Reference:
    def __init__(self):
        self.response=""
    def clear(self):
        self.response=""

reference=Reference()
# Load Env variable
load_dotenv()
LLM_API_KEY=os.getenv("LLM_API_KEY")
LLM_MODEL=os.getenv("LLM_MODEL")
LLM_URL=os.getenv("LLM_URL")



#  Ai assistent reply your message
@router.message(~filters.Command(commands=["start", "help","feture","clear"]))
async def AI_chat_bot(message: types.Message) -> None:

    try:
        async with httpx.AsyncClient(timeout=20) as client:
            response= await client.post(f"{LLM_URL}",
                json={
                "model": f"{LLM_MODEL}",
                "messages": [
                    {"role": "system", "content":"You are a concise AI assistant. Reply directly and briefly. Add extra points only if necessary. Avoid long explanations. give me in plain text format no styleing. if require give only one link no extra",},
                    {"role": "assistant", "content": reference.response},
                    {"role": "user", "content": message.text}
                    ],
                },
                headers={
                "Authorization": f"Bearer {LLM_API_KEY}",
                },
            )
            data=response.json()
            formated=markdowwn_to_html_format(data["choices"][0]["message"]["content"])
            await message.reply(formated,parse_mode="HTML")
            reference.response=data["choices"][0]["message"]["content"]

    except Exception as e:
        await message.answer(f"Error: {e}")
