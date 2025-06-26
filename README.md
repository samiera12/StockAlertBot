# 📈 Stock Alert Bot

This is a Python bot that tracks stock prices using [yfinance](https://pypi.org/project/yfinance/) and sends alerts when a threshold is crossed.

## 🔧 Features
- Real-time stock tracking
- Customizable thresholds
- Expandable for email, Telegram, or SMS alerts

## 🚀 How to Use
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
2. Run the bot
   ```bash
   python main.py
   
## 📦 Requirements
- Python 3.x
- yfinance

## ⚙️ How It Works
- Uses yfinance.Ticker("AAPL").history() to fetch real-time prices
- Checks if the latest closing price is above your custom threshold
- Alerts in the terminal if it is above



