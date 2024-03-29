from fastapi import FastAPI, Request
import logging
from gitlab import Gitlab

app = FastAPI()

logging.basicConfig(filename='events.log', level=logging.INFO)

@app.post("/webhook")
async def webhook(request: Request):
    body = await request.json()
    event_type = request.headers.get('X-Gitlab-Event')
    if event_type == 'Push Hook':
        logging.info(f"Push event detected: {body}")
    elif event_type == 'Merge Request Hook':
        logging.info(f"Merge Request event detected: {body}")
    return {"status": "ok"}