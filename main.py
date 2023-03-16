# Simulate the trading environment
import sys
from datamodel import *
from sample_trade import SampleTrade
from data_dump_trader import Trader
import traceback

def run_sample() -> int:
    return 0


def run_basic_test() -> int:
    trader = Trader()
    trader.run(SampleTrade)
    return 0

if __name__ == '__main__':
    print("============ Debugging mode =============") 
    if sys.argv[1] == 'sample':
        print("=== Running sample test \n")
        try:
            run_basic_test()
        except Exception as err:
            print(traceback.format_exc())
            print(err)