from binance.enums import *
from bot.client import get_client
from bot.logging_config import logger

client = get_client()


def place_order(symbol, side, order_type, quantity, price=None):
    try:

        if order_type == "MARKET":
            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type=FUTURE_ORDER_TYPE_MARKET,
                quantity=quantity
            )

        elif order_type == "LIMIT":
            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type=FUTURE_ORDER_TYPE_LIMIT,
                quantity=quantity,
                price=price,
                timeInForce="GTC"
            )

        logger.info(order)

        return order

    except Exception as e:
        logger.error(str(e))
        raise