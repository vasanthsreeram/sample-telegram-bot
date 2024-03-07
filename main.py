import os
from fastapi import FastAPI, Request
import requests
from dotenv import load_dotenv

load_dotenv()  # variables from .env
API_KEY = os.environ.get("TELEGRAM_API_KEY")

app = FastAPI()

@app.post("/webhook")
async def webhook(req: Request):
    print("something is detected")
    body = await req.json()
    if 'message' not in body:
        return print('No message found', body)
    bm = body['message']
    if 'text' not in bm:
        return print('No text found', body)
    print("valid text wow")
    chat_id = bm['chat']['id']
    text = bm['text']
    # Send echo message
    url = f"https://api.telegram.org/bot{API_KEY}/sendMessage"
    payload = {"chat_id": chat_id,
        "text": text}
    response = requests.post(url, json=payload)
    print("sent back")
    return response.json()
