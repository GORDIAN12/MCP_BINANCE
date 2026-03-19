from fastapi import FastAPI
from agent.analyst import CryptoAgent

app = FastAPI()
agent = CryptoAgent()

@app.get("/analyze")
def analyze():
    return agent.run()

@app.get("/price")
def price():
    return {"price": agent.run()["price"]}