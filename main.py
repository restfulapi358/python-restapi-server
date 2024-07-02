from fastapi import FastAPI
from fastapi.responses import JSONResponse
import uvicorn
import signal
import os
import threading
import time



# Create FastAPI instance
app = FastAPI()

# Define a route
@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

# Define a route
@app.get("/sayHello")
def read_root():
    return {"message": "Hello, World!"}


@app.get("/pi")
def read_root(r: Optional[float] = None):
    pi_value = 3.142
    if r is None:
        return {"message": pi_value}
    else:
        result = pi_value * r * r
        return {"message": result}


@app.post("/shutdown")
def shutdown():
    def shutdown_server():
        time.sleep(1)
        os.kill(os.getpid(), signal.SIGINT)
    
    threading.Thread(target=shutdown_server).start()
    return {"message": "Server is shutting down..."}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)
