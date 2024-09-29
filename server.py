from fastapi import FastAPI
from multiprocessing import Process
import time
from main import main
import asyncio

app = FastAPI()

def run_forever():
    asyncio.run(main())

def start_process():
    p = Process(target=run_forever)
    p.start()
    return p

@app.get("/")
async def root():
    return {"status": "ok"}

if __name__ == "__main__":
    process = start_process()

    import uvicorn
    uvicorn.run(app)

    process.join()
