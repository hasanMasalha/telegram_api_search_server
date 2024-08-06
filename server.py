from fastapi import FastAPI, HTTPException
from telethon import TelegramClient
from telethon.tl.functions.contacts import SearchRequest
from telethon.tl.types import InputPeerEmpty
from telethon.sync import TelegramClient
from telethon import functions, types
from telegram import Update
import os


app = FastAPI()

# Replace with your own values
api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')
bot_token = os.getenv('BOT_TOKEN')
phone_number = os.getenv('phone_number')

client = TelegramClient('session_name', api_id, api_hash)

@app.on_event("startup")
async def startup_event():
    await client.connect()
    if not await client.is_user_authorized():
        await client.send_code_request(phone_number)
        await client.sign_in(phone_number, input('Enter the code: '))

@app.on_event("shutdown")
async def shutdown_event():
    await client.disconnect()

@app.get("/search_groups/")
async def search_groups(keyword: str):
   
        try:
            result = await client(functions.contacts.SearchRequest(
            q=str(keyword),
            limit=10,
            ))
            groups = []
            for chat in result.chats:
                link = f"https://t.me/{chat.username}" if chat.username else "No link available"
                groups.append({"title": chat.title, "link": link})
            return {"groups": groups}
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
