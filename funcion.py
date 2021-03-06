import requests
_ENDPOINT = "https://api.binance.com"


def _url(api):
    return _ENDPOINT+api

    def get_price(cripto):
        return requests.get(_url("/api/v3/ticker/price?symbol="+cripto))

    def esmoneda(cripto):
        criptos = ["BTC", "BBC", "LTC", "ETC", "XRP"]
        return cripto in criptos


def get_price(cripto):
    return requests.get(_url("/api/v3/ticker/price?symbol="+cripto))

    def esnumero(numero):
        return numero.replace('.', '', 1).isdigit()

    monedas = []
    cantidades = []
    cotizaciones = []
    i = 0


def esmoneda(cripto):
    criptos = ["BTC", "BCC", "LTC", "ETH", "ETC", "XRP"]
    return cripto in criptos


def esnumero(numero):
    return numero.replace('.', '', 1).isdigit()


monedas = []
cantidades = []
cotizaciones = []
i = 0
while i < 3:
    moneda = input("ingrese el nombre de la moneda: ")
    while not esmoneda(moneda):
        print("moneda invalida.")
        monedas = input("ingrese el nombre de la moneda: ")
    else:
        monedas.append(moneda)
        data = get_price(moneda+"USDT").json()
        cotizaciones.append(float(data["price"]))
        cantidad = input("indique la cantidad de "+moneda+": ")
        while not esnumero(cantidad):
            cantidad = input("indique la cantidad de "+moneda+": ")
        else:
            cantidades.append(cantidad)
    i += 1

i = 0
total = 0

while i < 3:
    total += cantidades[i]*cotizaciones[i]
    print("moneda: ", monedas[i],
          ", cantidad: ", cantidades[i],
          ", cotizaciones: ", cotizaciones[i],
          ", cantidad de USDT: ", cantidades[i]*cotizaciones[i])
    i += 1
print("total en USDT es: ", str(total))
