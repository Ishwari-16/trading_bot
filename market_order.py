from dotenv import load_dotenv
import os
from binance.um_futures import UMFutures

load_dotenv()

client = UMFutures(
    key=os.getenv("BINANCE_API_KEY"),
    secret=os.getenv("BINANCE_SECRET_KEY"),
    base_url="https://testnet.binancefuture.com"
)

try:
    order = client.new_order(
        symbol="BTCUSDT",
        side="BUY",
        type="MARKET",
        quantity=0.001
    )

    print("✅ MARKET Order Successful")
    print(order)

except Exception as e:
    print("❌ MARKET Order Failed")
    print(e)