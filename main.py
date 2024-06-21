from fastapi import FastAPI
from fastapi.responses import JSONResponse
import uvicorn
import signal
import os


# Create FastAPI instance
app = FastAPI()

# Define a route
@app.get("/")
def read_root():
    return {"message": "Hello, World!"}


@app.post("/shutdown")
def shutdown():
    def shutdown_server():
        time.sleep(1)
        os.kill(os.getpid(), signal.SIGINT)
    
    threading.Thread(target=shutdown_server).start()
    return {"message": "Server is shutting down..."}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8001)
