from dotenv import load_dotenv
import os
from binance.um_futures import UMFutures

load_dotenv()

client = UMFutures(
    key=os.getenv("BINANCE_API_KEY"),
    secret=os.getenv("BINANCE_SECRET_KEY"),
    base_url="https://testnet.binancefuture.com"
)

order = client.query_order(
    symbol="BTCUSDT",
    orderId=18297390837   # Replace with your latest orderId
)

print(order)