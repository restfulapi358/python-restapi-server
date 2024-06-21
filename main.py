from fastapi import FastAPI

# Create FastAPI instance
app = FastAPI()

# Define a route
@app.get("/")
def read_root():
    return {"message": "Hello, World!"}


@app.post("/shutdown")
def shutdown():
    def shutdown_server():
        pid = os.getpid()
        os.kill(pid, signal.SIGINT)
    
    shutdown_server()
    return JSONResponse(content={"message": "Server is shutting down..."})

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
