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

<img width="1090" height="367" alt="Screenshot 2026-02-19 at 11 19 11 PM" src="https://github.com/user-attachments/assets/2641e46b-0e32-4db9-a107-b3f0ebd0634f" />

<br>

<img width="1090" height="377" alt="Screenshot 2026-02-19 at 11 19 31 PM" src="https://github.com/user-attachments/assets/fa10289e-b9d2-458d-917e-f36af9110eef" />

<br>

<img width="1090" height="458" alt="Screenshot 2026-02-19 at 11 31 37 PM" src="https://github.com/user-attachments/assets/a1ccb4ad-dfc5-4c92-a42b-280a4cea9943" />

