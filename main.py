from fastapi import FastAPI

# Create FastAPI instance
app = FastAPI()

# Define a route
@app.get("/")
def read_root():
    return {"message": "Hello, World!"}