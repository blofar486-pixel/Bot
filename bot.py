import requests
import time

BOT_TOKEN = "8328605174:AAHO8vuYXUYJx5226E15ZqxNc9rXPcKa1Ts"
CHAT_ID = "8328605174"

PAIRS = {
    "EURUSD": "EURUSD=X",
    "GBPUSD": "GBPUSD=X",
    "USDJPY": "JPY=X",
    "BTCUSD": "BTC-USD",
    "ETHUSD": "ETH-USD"
}

def send_telegram(msg):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": msg})


def get_price(symbol):
    try:
        url = f"https://query1.finance.yahoo.com/v8/finance/chart/{symbol}?interval=5m&range=1d"
        r = requests.get(url).json()
        result = r["chart"]["result"][0]
        return result["meta"]["regularMarketPrice"]
    except:
        return None


while True:
    msg = "📊 LIVE MARKET UPDATE\n\n"

    for name, symbol in PAIRS.items():
        price = get_price(symbol)

        if price:
            msg += f"{name}: {price}\n"

    send_telegram(msg)
    print("sent")

    time.sleep(300)
