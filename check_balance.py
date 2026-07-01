from dotenv import load_dotenv
import os
from binance.um_futures import UMFutures

load_dotenv()

client = UMFutures(
    key=os.getenv("BINANCE_API_KEY"),
    secret=os.getenv("BINANCE_SECRET_KEY"),
    base_url="https://testnet.binancefuture.com"
)

balances = client.balance()

for balance in balances:
    if balance["asset"] == "USDT":
        print(balance)