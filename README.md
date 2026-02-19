# Binance Futures Trading Bot (Testnet)

A minimal Python CLI application to place MARKET and LIMIT orders on Binance USDT-M Futures.

## Features
- MARKET and LIMIT orders
- BUY / SELL support
- CLI arguments (argparse)
- Optional interactive menu mode (bonus)
- Input validation and error handling
- File-based logging

## Setup

1. Create virtual environment
```bash
python -m venv .venv
source .venv/bin/activate   #macos
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

3. Configure environment variables (create a .env file at project root)
```bash
BINANCE_API_KEY=your_api_key
BINANCE_API_SECRET=your_api_secret
```


## CLI Arguments
- `--symbol` : The market being traded (Example: BTCUSDT)
- `--side` : BUY or SELL
- `--type` : MARKET or LIMIT
- `--quantity` : Order quantity
- `--price` : Required for LIMIT orders


## Usage 

1. Place a MARKET order
```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.003
```

2. Place a LIMIT order
```bash
python cli.py --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.005 --price 30000
```

3. Interactive menu
```bash
python cli.py
```

## Logging

Logs are written to:[`logs/trading_bot.log`](logs/trading_bot.log)

The log file includes:
- API request summaries
- Order responses
- Error messages


## Screenshots 

