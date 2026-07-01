import argparse
from bot.orders import place_order
from bot.validators import (
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price
)

def main():
    parser = argparse.ArgumentParser(
        description="Binance Futures Testnet Trading Bot"
    )

    parser.add_argument("--symbol", required=True, help="Trading Symbol (e.g., BTCUSDT)")
    parser.add_argument("--side", required=True, help="BUY or SELL")
    parser.add_argument("--type", required=True, help="MARKET or LIMIT")
    parser.add_argument("--quantity", required=True, help="Order Quantity")
    parser.add_argument("--price", help="Price (Required for LIMIT Order)")

    args = parser.parse_args()

    try:
        symbol = args.symbol.upper()
        side = validate_side(args.side)
        order_type = validate_order_type(args.type)
        quantity = validate_quantity(args.quantity)
        price = validate_price(args.price)

        if order_type == "LIMIT" and price is None:
            raise ValueError("LIMIT order requires --price")

        print("\n========== ORDER REQUEST ==========")
        print(f"Symbol     : {symbol}")
        print(f"Side       : {side}")
        print(f"Type       : {order_type}")
        print(f"Quantity   : {quantity}")

        if price:
            print(f"Price      : {price}")

        order = place_order(
            symbol=symbol,
            side=side,
            order_type=order_type,
            quantity=quantity,
            price=price
        )

        print("\n========== ORDER RESPONSE ==========")
        print("Order ID :", order.get("orderId"))
        print("Status   :", order.get("status"))
        print("Executed :", order.get("executedQty"))
        print("Avg Price:", order.get("avgPrice", "N/A"))

        print("\n✅ Order Placed Successfully!")

    except Exception as e:
        print("\n❌ Error:", e)

if __name__ == "__main__":
    main()