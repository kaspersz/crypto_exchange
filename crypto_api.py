import requests

coinsList = None
def getCoinsList():
    global coinsList
    response = requests.get("https://api.coingecko.com/api/v3/coins/list?include_platform=true")

    if response.ok == True:
        data = response.json()
        print(data[0])
        coinsList = data
    print(len(data))

def findCoinBySymbol(symbol):
    symbol = symbol.lower().strip()
    for coin in coinsList:
        if coin["symbol"] == symbol:
            return coin
    else: return None
getCoinsList()
coinData = findCoinBySymbol("ETH")


def getPriceOfTheCoin(coinData):
    id = coinData["id"]
    print(id)
    response = requests.get("https://api.coingecko.com/api/v3/coins/"+str(id))
    data = response.json()
    print(data["market_data"]["current_price"]["usd"])
    return data

getPriceOfTheCoin(coinData)


def getPriceOfAnotherMethod(coinData, currency):
    id = coinData["id"]
    response = requests.get("https://api.coingecko.com/api/v3/simple/price?ids="+id+"&vs_currencies="+currency)
    dataCurr = response.json()
    return dataCurr[id][currency]

print(getPriceOfAnotherMethod(coinData, "usd"))
