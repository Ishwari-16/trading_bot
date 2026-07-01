# Binance Futures Testnet Trading Bot

A Python command-line application that places **MARKET** and **LIMIT** orders on the **Binance Futures Testnet (USDT-M)**. The project demonstrates a modular architecture, input validation, logging, and exception handling.

---

## Features

- Place **MARKET** orders
- Place **LIMIT** orders
- Supports both **BUY** and **SELL**
- Command Line Interface (CLI) using `argparse`
- Input validation
- API error handling
- Request and response logging
- Modular and reusable project structure

---

## Project Structure

```
trading_bot/
│
├── bot/
│   ├── __init__.py
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   ├── logging_config.py
│   └── cli.py
│
├── logs/
│   └── trading.log
│
├── requirements.txt
├── README.md
├── .env.example
└── .gitignore
```

---

## Requirements

- Python 3.10 or higher
- Binance Futures Testnet account
- Binance API Key
- Binance Secret Key

---

## Installation

Clone the repository:

```bash
git clone https://github.com/<your-github-username>/trading_bot.git

cd trading_bot
```

Create a virtual environment:

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the project root.

Example:

```env
BINANCE_API_KEY=YOUR_API_KEY
BINANCE_SECRET_KEY=YOUR_SECRET_KEY
```

**Do not commit your actual `.env` file to GitHub.**

---

## Usage

### Place a MARKET Order

```bash
python -m bot.cli --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

---

### Place a LIMIT Order

```bash
python -m bot.cli --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 70000
```

---

## CLI Arguments

| Argument | Description | Required |
|----------|-------------|----------|
| --symbol | Trading Symbol (e.g. BTCUSDT) | Yes |
| --side | BUY or SELL | Yes |
| --type | MARKET or LIMIT | Yes |
| --quantity | Order Quantity | Yes |
| --price | Limit Price (LIMIT orders only) | No (Required for LIMIT) |

---

## Validation

The application validates:

- Trading side (BUY / SELL)
- Order type (MARKET / LIMIT)
- Positive quantity
- Positive limit price
- LIMIT orders require a price

---

## Logging

The application logs:

- API requests
- API responses
- Successful orders
- Errors and exceptions

Log file:

```
logs/trading.log
```

---

## Sample Output

### MARKET Order

```
========== ORDER REQUEST ==========
Symbol     : BTCUSDT
Side       : BUY
Type       : MARKET
Quantity   : 0.001

========== ORDER RESPONSE ==========
Order ID : 18300943578
Status   : FILLED
Executed : 0.001
Avg Price: 60117.80

✅ Order Placed Successfully!
```

---

### LIMIT Order

```
========== ORDER REQUEST ==========
Symbol     : BTCUSDT
Side       : SELL
Type       : LIMIT
Quantity   : 0.001
Price      : 70000

========== ORDER RESPONSE ==========
Order ID : 18301024621
Status   : NEW
Executed : 0.000
Avg Price: N/A

✅ Order Placed Successfully!
```

---

## Assumptions

- Binance Futures Testnet account is activated.
- API credentials are valid.
- Internet connection is available.
- Testnet account contains sufficient USDT balance.

---

## Technologies Used

- Python 3
- Binance Futures Connector
- argparse
- python-dotenv
- logging

---

## Author

**Ishwari Barole**
