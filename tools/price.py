from binance.client import Client
import os
from dotenv import load_dotenv
load_dotenv()

API_KEY=os.getenv("API_KEY")
SECRET_KEY=os.getenv("SECRET_KEY")

client= Client(API_KEY, SECRET_KEY)

def get_price(symbol="BTCUSDT"):
    data=client.get_symbol_ticker(symbol=symbol)
    return float(data["price"])

print(get_price)