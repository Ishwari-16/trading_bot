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
    account = client.account()

    print("✅ Connected Successfully")
    print("Account Alias:", account.get("feeTier"))
except Exception as e:
    print("❌ Connection Failed")
    print(e)