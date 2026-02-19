from binance.client import Client
from binance.exceptions import BinanceAPIException, BinanceRequestException

from bot.logger import get_logger

logger = get_logger(__name__)


def place_order(
    client: Client,
    symbol: str,
    side: str,
    order_type: str,
    quantity: float,
    price: float | None = None,
):
    try:
        logger.info(
            f"Placing order | symbol={symbol}, side={side}, type={order_type}, "
            f"qty={quantity}, price={price}"
        )

        if order_type == "MARKET":
            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type=order_type,
                quantity=quantity,
            )

        elif order_type == "LIMIT":
            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type=order_type,
                quantity=quantity,
                price=price,
                timeInForce="GTC",
            )

        else:
            raise ValueError("Unsupported order type")

        logger.info(f"Order response: {order}")
        return order

    except (BinanceAPIException, BinanceRequestException) as e:
        logger.error(f"Binance API error: {e}")
        raise

    except Exception as e:
        logger.exception("Unexpected error while placing order")
        raise
