import requests

BASE_URL = "https://fapi.binance.com"

def get_top_coins():
    url = BASE_URL + "/fapi/v1/ticker/24hr"
    data = requests.get(url).json()

    coins = []

    for c in data:
        try:
            if not c["symbol"].endswith("USDT"):
                continue

            change = float(c["priceChangePercent"])
            volume = float(c["quoteVolume"])

            if volume < 20000000:
                continue

            if 2 <= change <= 8:
                coins.append(c)

        except:
            pass

    coins = sorted(
        coins,
        key=lambda x: float(x["quoteVolume"]),
        reverse=True
    )

    print("TOP 10 COINS")

    for i, c in enumerate(coins[:10], 1):
        print(
            i,
            c["symbol"],
            c["lastPrice"],
            c["priceChangePercent"] + "%"
        )

if __name__ == "__main__":
    get_top_coins()
