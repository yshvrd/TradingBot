import os
from binance.client import Client
from dotenv import load_dotenv

from bot.logger import get_logger

logger = get_logger(__name__)

FUTURES_DEMO_BASE_URL = "https://demo-fapi.binance.com"

def get_binance_client() -> Client:
    load_dotenv()

    api_key = os.getenv("BINANCE_API_KEY")
    api_secret = os.getenv("BINANCE_API_SECRET")

    if not api_key or not api_secret:
        logger.error("Missing Binance API credentials in environment")
        raise RuntimeError("BINANCE_API_KEY or BINANCE_API_SECRET not set")

    client = Client(api_key, api_secret, testnet=True)

    client.FUTURES_URL = FUTURES_DEMO_BASE_URL

    logger.info("Binance Futures demo client initialized")

    return client
