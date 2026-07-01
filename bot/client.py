import os
from dotenv import load_dotenv
from binance.um_futures import UMFutures

load_dotenv()

def get_client():
    return UMFutures(
        key=os.getenv("BINANCE_API_KEY"),
        secret=os.getenv("BINANCE_SECRET_KEY"),
        base_url="https://testnet.binancefuture.com"
    )