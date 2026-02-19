import argparse
import sys

from bot.binance_client import get_binance_client
from bot.orders import place_order
from bot.validators import (
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price,
)
from bot.logger import get_logger

logger = get_logger(__name__)


def interactive_prompt():
    print("\n--- Interactive Order Menu ---")

    symbol = input("Enter symbol (Example: BTCUSDT): ").strip()

    side_choice = input("Select side [1] BUY [2] SELL: ").strip()
    side = "BUY" if side_choice == "1" else "SELL"

    type_choice = input("Select order type [1] MARKET [2] LIMIT: ").strip()
    order_type = "MARKET" if type_choice == "1" else "LIMIT"

    quantity = float(input("Enter quantity: ").strip())

    price = None
    if order_type == "LIMIT":
        price = float(input("Enter price: ").strip())

    return symbol, side, order_type, quantity, price


def main():
    parser = argparse.ArgumentParser(description="Binance Futures Trading Bot")

    parser.add_argument("--symbol", type=str)
    parser.add_argument("--side", type=str)
    parser.add_argument("--type", dest="order_type", type=str)
    parser.add_argument("--quantity", type=float)
    parser.add_argument("--price", type=float)

    args = parser.parse_args()

    try:
        # If no args provided → interactive bonus mode
        if not any(vars(args).values()):
            symbol, side, order_type, quantity, price = interactive_prompt()
        else:
            symbol = args.symbol
            side = args.side
            order_type = args.order_type
            quantity = args.quantity
            price = args.price

        # Validation layer
        side = validate_side(side)
        order_type = validate_order_type(order_type)
        quantity = validate_quantity(quantity)
        price = validate_price(price, order_type)

        print("\n--- Order Summary ---")
        print(f"Symbol: {symbol}")
        print(f"Side: {side}")
        print(f"Type: {order_type}")
        print(f"Quantity: {quantity}")
        if order_type == "LIMIT":
            print(f"Price: {price}")

        client = get_binance_client()

        order = place_order(
            client=client,
            symbol=symbol,
            side=side,
            order_type=order_type,
            quantity=quantity,
            price=price,
        )

        print("\n--- Order Response ---")
        print(f"Order ID: {order.get('orderId')}")
        print(f"Status: {order.get('status')}")
        print(f"Executed Qty: {order.get('executedQty')}")
        print(f"Avg Price: {order.get('avgPrice')}")

        print("\nOrder placed successfully ✅")

    except Exception as e:
        print(f"\nOrder failed ❌: {e}")
        logger.error(f"CLI error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
