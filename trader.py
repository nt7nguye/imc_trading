from typing import *
from datamodel import *

# refactor
MAX_QUANT = 20

class RollingAverage:
    def __init__(self, window_size):
        self.window_size = window_size
        self.values = [0] * window_size
        self.sum = 0
        self.idx = 0
    
    def add_value(self, value):
        self.sum -= self.values[self.idx]
        self.sum += value
        self.values[self.idx] = value
        self.idx = (self.idx + 1) % self.window_size
    
    def get_average(self):
        return self.sum / min(len(self.values), self.window_size)


class ExponentialMovingAverage:
    def __init__(self, window_size):
        self.window_size = window_size
        self.alpha = 2 / (window_size + 1)
        self.value = 0
    
    def add_value(self, value):
        self.value = self.alpha * value + (1 - self.alpha) * self.value
    
    def get_average(self):
        return self.value

class Trader:
    ave = {
        "BANANAS": ExponentialMovingAverage()        
    } 

    def run(self, state: TradingState) -> Dict[str, List[Order]]:
        result = {}
        for product, depth in state.order_depths.items():
            # try simple +1 buy price and -1 sell price
            # Max buy price
            max_buy = max(depth.buy_orders.keys())
            max_buy_vol = depth.buy_orders[max_buy]

            min_sell = min(depth.sell_orders.keys())
            min_sell_vol = depth.sell_orders[min_sell]

            # Our inventory
            position = 0 if state.position.get(product) is None else state.position[product]

            result[product] = []

            if product == "BANANAS":

                if position <= 0:
                    # buy
                    buy_order = Trade(product, max_buy + 1, MAX_QUANT if position == 0 else -position)
                    result[product].append(buy_order)
                else:
                    # sell
                    sell_order = Trade(product, min_sell - 1, -position)
                    result[product].append(sell_order)
            else:
                continue
                # Is product == symbol ? TODO: check
                if max_buy < 9999:
                    buy_order = Trade(product, max_buy + 1, MAX_QUANT - position)
                    result[product].append(buy_order)
                if min_sell > 10001:
                    sell_order = Trade(product, min_sell - 1, -MAX_QUANT - position)
                    result[product].append(sell_order)
        return result