from functools import reduce

def assert_valid_input(change, coins):
    if any(isinstance(number, float) for number in [change] + coins):
        raise TypeError

    if any(coin <= 0 for coin in coins) or change < 0:
        raise ValueError

def number_of_coins(change, coins):
    assert_valid_input(change, coins)
    return reduce(lambda change_and_count, coin: (change_and_count[0] % coin, change_and_count[1] + change_and_count[0] // coin), coins, (change, 0))[1]