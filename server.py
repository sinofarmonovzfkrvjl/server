from fastapi import FastAPI
from multiprocessing import Process
import time
from main import main
import asyncio

app = FastAPI()

# Function to run another Python file's logic
def run_forever():
    asyncio.run(main())

# Function to start the background process
def start_process():
    p = Process(target=run_forever)
    p.start()
    return p

# Route for testing server is alive
@app.get("/")
async def root():
    return {"status": "ok"}

if __name__ == "__main__":
    # Start the background process
    process = start_process()

    # Run the FastAPI server
    import uvicorn
    uvicorn.run(app)

    # Join the process when the server stops
    process.join()
