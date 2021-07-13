from functools import reduce

def number_of_coins(change, coins):
    def exchange_coin(change_and_count, coin):
        change, count = change_and_count
        return change % coin, count + change // coin, 

    change, count = reduce(exchange_coin, coins, (change, 0))
    return count