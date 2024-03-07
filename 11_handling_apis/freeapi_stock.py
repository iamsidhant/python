
import requests

def fetch_random_stock_freeapi():
    url = "https://api.freeapi.app/api/v1/public/stocks/stock/random"
    response = requests.get(url)
    data = response.json()

    if data["success"] and "data" in data:
        user_data = data["data"]
        Name = user_data["Name"]
        MarketCap = user_data["MarketCap"]
        return Name, MarketCap
    else:
        raise Exception("Failed to fetch user data")


def main():
    try:
        Name, MarketCap = fetch_random_stock_freeapi()
        print(f"Name: {Name}  \nMarketCap: {MarketCap}")
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()    
