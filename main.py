import yfinance as yf
import time

def check_price(ticker, threshold):
    stock = yf.Ticker(ticker)
    price = stock.history(period="1d",interval="1m")['Close'].iloc[-1]
    print(f"{ticker} current price: {price}")
    if price > threshold:
        print(f"🚨 {ticker} crossed the threshold of {threshold}!")

if __name__ == "__main__":
    while True:
        check_price("AAPL", 200)
        time.sleep(60)

