import os
from fastapi import FastAPI, Request
import requests
from dotenv import load_dotenv
import logging
logging.basicConfig(level=logging.INFO)

load_dotenv()  # This loads the environment variables from .env


API_KEY = os.environ.get("TELEGRAM_API_KEY")
logging.info("app started")
app = FastAPI()

@app.post("/webhook")
async def webhook(req: Request):
    logging.info("something is detected")
    body = await req.json()
    if 'message' not in body:
        return logging.info('No message found', body)
    bm = body['message']
    if 'text' not in bm:
        return logging.info('No text found', body)
    logging.info("valid text wow")
    chat_id = bm['chat']['id']
    text = bm['text']
    # Send echo message
    url = f"https://api.telegram.org/bot{API_KEY}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": text
    }
    response = requests.post(url, json=payload)
    logging.info("sent back")
    return response.json()