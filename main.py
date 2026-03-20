from fastapi import FastAPI

app  = FastAPI(title="Task Manager API")

@app.get("/")
def Home():
    return {"message" : "Your API is Running Now"}

