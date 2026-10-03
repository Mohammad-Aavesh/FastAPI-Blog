from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()

@app.get("/")
def home():
    return {"Message":"Hello"}
