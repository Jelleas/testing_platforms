def assert_valid_input(change, coins):
    if any(isinstance(number, float) for number in [change] + coins):
        raise TypeError

    if any(coin <= 0 for coin in coins):
        raise ValueError

    if change <= 0:
        raise ValueError

def number_of_coins(change, coins):
    assert_valid_input(change, coins)

    if not coins:
        return 0

    count = 0
    coins = sorted(coins)[::-1]

    for coin in coins:
        while change - coin >= 0:
            change -= coin
            count += 1

    return count
