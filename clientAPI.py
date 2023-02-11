from datetime import datetime, timedelta

from alpaca.trading.client import TradingClient
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce
from alpaca.data.historical import CryptoHistoricalDataClient
from alpaca.data.requests import CryptoBarsRequest
from alpaca.data.timeframe import TimeFrame

API_KEY = 'PKWRE9AKDSDX7AH2UJNB'
SECRET_KEY = 'i2mYCn7F0xl39iSCVYVcLfiDe6vDwfgm8CBEUsCG'


class InitialiseClient():
    def __init__(self):
        self.trade = TradingClient(API_KEY, SECRET_KEY, paper=True)
        self.data = CryptoHistoricalDataClient()

    def display_position(self):
        positions = self.trade.get_all_positions()
        i = 1
        for position in positions:
            print(f"Position {i} informations : ")
            for property_name, value in position:
                print(f"\"{property_name}\": {value}")
            if position != positions[-1]:
                print("---------------------------------------------")
            i = i + 1

    def get_data(self, symbol="BTC/USD", start=datetime.now() - timedelta(days=7), end=datetime.now(), timeframe=TimeFrame.Day):
        if not isinstance(start, datetime):
            start = datetime.fromtimestamp(start)
        if not isinstance(end, datetime):
            end = datetime.fromtimestamp(end)
        request_params = CryptoBarsRequest(
            symbol_or_symbols=[symbol],
            timeframe=timeframe,
            start=start,
            end=end
        )
        return self.data.get_crypto_bars(request_params).df

    def order(self, qty, symbol="ETH/USD", order_type="BUY"):
        if order_type == "BUY":
            order_type = OrderSide.BUY
        else:
            order_type = OrderSide.SELL
        market_order_data = MarketOrderRequest(
            symbol=symbol,
            qty=qty,
            side=order_type,
            time_in_force=TimeInForce.GTC
        )
        return self.trade.submit_order(market_order_data)
