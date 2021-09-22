_ENDPOINT = "https://api.binance.com"


def _url(api):
    return _ENDPOINT+api

    def get_price(cripto):
        return requests.get(_url("/api/v3/ticker/price?symbol="+cripto))

    def esmoneda(cripto):
        criptos = ["BTC", "BBC", "LTC", "ETC", "XRP"]
        return cripto in criptos

    def esnumero(numero):
        return numero.replace('.', '', 1).isdigit()

    monedas = []
    cantidades = []
    cotizaciones = []
    i = 0
