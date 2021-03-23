class CurrencyPair:
    def __init__(self, /, id, code, scale):
        self.id = id
        self.code = code
        self.scale = scale
        self.mark_price = None
        self.sell_price = None
        self.buy_price = None
        self.unreliable = None

    def on_update(self):
        pass

    def __repr__(self):
        return f'CurrencyPair(id={self.id}, code={self.code})'

    def __str__(self):
        return self.code

CurrencyPair.BTC_USD = CurrencyPair(id=1, code='BTC/USD', scale=4)
CurrencyPair.ETH_USD = CurrencyPair(id=2, code='ETH/USD', scale=4)
CurrencyPair.DGTX_ETH = CurrencyPair(id=3, code='DGTX/ETH', scale=8)
CurrencyPair.DGTX_BTC = CurrencyPair(id=4, code='DGTX/BTC', scale=8)
CurrencyPair.XRPx10000_USD = CurrencyPair(id=6, code='XRP/USD_10K', scale=4)
CurrencyPair.XAU_USD = CurrencyPair(id=7, code='XAU/USD', scale=4)
CurrencyPair.XRP_USD = CurrencyPair(id=8, code='XRP/USD', scale=5)
CurrencyPair.AAPL = CurrencyPair(id=19, code='AAPL', scale=4)
CurrencyPair.FB = CurrencyPair(id=20, code='FB', scale=4)
CurrencyPair.AMZN = CurrencyPair(id=21, code='AMZN', scale=4)
CurrencyPair.SPY = CurrencyPair(id=24, code='SPY', scale=4)
CurrencyPair.EUR_USD = CurrencyPair(id=26, code='EUR/USD', scale=4)
CurrencyPair.USD_JPY = CurrencyPair(id=28, code='USD/JPY', scale=4)
CurrencyPair.USD_RUB = CurrencyPair(id=29, code='USD/RUB', scale=4)
CurrencyPair.BTC_DUSD = CurrencyPair(id=36, code='BTC/UDSD', scale=4)
CurrencyPair.ETH_BTC = CurrencyPair(id=37, code='ETH/BTC', scale=8)
CurrencyPair.ETH_DUSD = CurrencyPair(id=38, code='ETH/DUSD', scale=4)
CurrencyPair.DUSD_USDC = CurrencyPair(id=39, code='DUSD/USDC', scale=4)
CurrencyPair.LINK_DUSD = CurrencyPair(id=40, code='LINK/DUSD', scale=4)
CurrencyPair.DGTX_DUSD = CurrencyPair(id=41, code='DGTX/DUSD', scale=4)
CurrencyPair.DGTX_LINK = CurrencyPair(id=42, code='DGTX/LINK', scale=4)
