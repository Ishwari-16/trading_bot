from bot.client import get_client
from bot.logging_config import logger

client = get_client()

def place_order(symbol, side, order_type, quantity, price=None):
    try:

        if order_type == "MARKET":
            order = client.new_order(
                symbol=symbol,
                side=side,
                type="MARKET",
                quantity=quantity
            )

        elif order_type == "LIMIT":
            order = client.new_order(
                symbol=symbol,
                side=side,
                type="LIMIT",
                quantity=quantity,
                price=price,
                timeInForce="GTC"
            )

        else:
            raise ValueError("Invalid Order Type")

        logger.info(order)
        return order

    except Exception as e:
        logger.error(str(e))
        raise