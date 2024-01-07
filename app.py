from fastapi import FastAPI, Request


# Install the required libraries


app = FastAPI()

@app.post("/webhook")
async def webhook(req:Request): # Handle incoming webhook requests from Telegram.
    """
    Args:
        req (Request): The incoming request object.

    Returns:
        None
    """

    
    body = await req.json() # pulls the body of the message

    if 'message' not in body: 
        return print('No message found', body)  # Check if 'message' key exists in the request body
    bm = body['message']

    if 'text' not in bm: 
        return print('No text found', body)  # Check if 'text' key exists in the message body

    return print(bm)




