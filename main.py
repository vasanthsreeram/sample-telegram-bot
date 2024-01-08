import os
from fastapi import FastAPI, Request
import requests
from dotenv import load_dotenv
import logging
logger = logging.getLogger('azure.mgmt.resource')

# Set the logging level for all azure-storage-* libraries
logger = logging.getLogger('azure.storage')
logger.setLevel(logging.INFO)

# Set the logging level for all azure-* libraries
logger = logging.getLogger('azure')
logger.setLevel(logging.ERROR)

print(
    f"Logger enabled for ERROR={logger.isEnabledFor(logging.ERROR)}, "
    f"WARNING={logger.isEnabledFor(logging.WARNING)}, "
    f"INFO={logger.isEnabledFor(logging.INFO)}, "
    f"DEBUG={logger.isEnabledFor(logging.DEBUG)}"
)

load_dotenv()  # This loads the environment variables from .env


# API_KEY = os.environ.get("TELEGRAM_API_KEY")
API_KEY = "6521636846:AAE7TmZnagfWQafUWC57MSELETXSITgeD88"
logging.error("app started, api key is " + API_KEY)
logging.info("app started, api key is " + API_KEY)
print("app started, api key is " + API_KEY)
app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.post("/webhook")
async def webhook(req: Request):
    logging.error("something is detected")
    body = await req.json()
    if 'message' not in body:
        return logging.error('No message found', body)
    bm = body['message']
    if 'text' not in bm:
        return logging.error('No text found', body)
    logging.error("valid text wow")
    chat_id = bm['chat']['id']
    text = bm['text']
    # Send echo message
    url = f"https://api.telegram.org/bot{API_KEY}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": text
    }
    response = requests.post(url, json=payload)
    logging.error("sent back")
    return response.json()