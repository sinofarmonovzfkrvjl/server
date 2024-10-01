from fastapi import FastAPI
from threading import Thread
import os

app = FastAPI()

@app.get("/")
async def root():
    Thread(target=run).start()
    return {"status": "ok"}

def run():
    while True:
        os.system("python main.py")