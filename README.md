# Binance Futures Testnet Trading Bot

## Overview
A Python CLI application that places MARKET and LIMIT orders on Binance Futures Testnet (USDT-M).

## Features
- Place MARKET Orders
- Place LIMIT Orders
- BUY & SELL support
- CLI using argparse
- Input Validation
- Logging
- Exception Handling

## Project Structure

```
trading_bot/
│
├── bot/
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   ├── logging_config.py
│   └── cli.py
│
├── logs/
├── requirements.txt
├── README.md
└── .env
```

## Installation

```bash
git clone <your-github-repository>
cd trading_bot

python -m venv venv

# Windows
venv\Scripts\activate

pip install -r requirements.txt
```

## Configure API

Create a `.env` file:

```
BINANCE_API_KEY=YOUR_API_KEY
BINANCE_SECRET_KEY=YOUR_SECRET_KEY
```

## Run MARKET Order

```bash
python -m bot.cli --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

## Run LIMIT Order

```bash
python -m bot.cli --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 120000
```

## Assumptions

- Binance Futures Testnet account is active.
- API keys are valid.
- Internet connection is available.
