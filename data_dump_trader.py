from typing import Dict, List
from datamodel import OrderDepth, TradingState, Order, Trade
import json

def dump_print(string: str):
    print(f"\nDUMP: {string}")

class Trader:
    def __init__(self):
        dump_print("Timestamp,Product,Buy Depth,Sell Depth,Trades")

    def run(self, state: TradingState) -> Dict[str, List[Order]]:
        """
        Only method required. It takes all buy and sell orders for all symbols as an input,
        and outputs a list of orders to be sent
        """
        timestamp = str(state.timestamp)
        products = list(state.listings.keys())

        for product in products:
            buy_depth = "{}"
            sell_depth = "{}"
            if state.order_depths.get(product) is not None:
                buy_depth = json.dumps(state.order_depths[product].buy_orders, separators=(";", ":"))
                sell_depth = json.dumps(state.order_depths[product].sell_orders, separators=(";", ":"))
            
            trades = "[]"
            if state.market_trades.get(product) is not None:
                trades = json.dumps(state.market_trades[product], separators=(";", ":"))
            #row = [timestamp, product, buy_depth, sell_depth, trades]
            row = [json.dumps(state.order_depths.get(product).buy_orders, default=lambda o: o.__dict__, sort_keys=True)]
            
            dump_print(','.join(row))
        return {}