from functools import reduce

def number_of_coins(change, coins):
    return reduce(lambda change_and_count, coin: (change_and_count[0] % coin, change_and_count[1] + change_and_count[0] // coin), coins, (change, 0))[1]