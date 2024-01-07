import os
from fastapi import FastAPI, Request
import requests

API_KEY = os.environ.get("TELEGRAM_API_KEY")
print("app started")
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
    payload = {
        "chat_id": chat_id,
        "text": text
    }
    response = requests.post(url, json=payload)
    print("sent back")
    return response.json()