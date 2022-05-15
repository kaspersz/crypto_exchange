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


print("WITAMY W CRYPTO_EXCHANGE")
while True:
    cryptoSymbol = input("Wybierz symbol krypto do kupienia lub exit zeby zakonczyc")
    if cryptoSymbol == "exit":
        break
    chosenCoin = findCoinBySymbol(cryptoSymbol)
    if chosenCoin == None:
        print("Wybrana kryptowaluta nie istnieje")
        continue
    else:
        print("Wybrales kryptowalute:" , chosenCoin["id"])
        currency = input("\nWybierz w jakiej walucie chcesz kupic: ")
        pricePerUnit = getPriceOfAnotherMethod(chosenCoin, currency)
        print("Cena jednej sztuki w", currency," to", pricePerUnit)
        number = input("Ile chcesz kupic? ")
        finalPrice = float(pricePerUnit) * float(number)
        print("Koszt zakupu danej ilosci kryptowaluty wynosi:", finalPrice)
        answer = input("Potwierdz jesli chcesz zakupic i wyjsc wpisujac 1, jesli chcesz zakupic i kontynowac zakupy wcisnij 2, 3 jesli chcesz zrezygnowac z zakupu, exit jesli chcesz opuscic kantor")
        if input == 1: 
            print("Dziekuje za zakupy")
            break
        elif input==2:
            print("dziekuje za zakupy, zaraz zostaniesz przeniesiony do menu wyboru kryptowaluty")
        elif input==3:
            continue
        elif input == "exit":
            break


