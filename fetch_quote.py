import requests

def lookup(symbol):
    """Look up quote for symbol."""

    # Contact API
    try:
        #api_key = os.environ.get("API_KEY")
        response = requests.get("https://cloud.iexapis.com/stable/stock/{symbol}/quote/latestPrice?token=sk_65fbcc2f2671478ca993d0fbf3c83ee8")
        #print(response.json())
        #response.raise_for_status()
    except requests.RequestException:
        return None

    # Parse response
    try:
        quote = response.json()
        print(quote)
        return {
            "name": quote["companyName"],
            "price": float(quote["latestPrice"]),
            "symbol": quote["symbol"]
        }
    except (KeyError, TypeError, ValueError):
        return None


print(lookup("AAPL"))
