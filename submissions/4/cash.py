def assert_valid_input(change, coins):
    if any(isinstance(number, float) for number in [change] + coins):
        raise TypeError

    if any(coin <= 0 for coin in coins):
        raise ValueError

def number_of_coins(change, coins):
    assert_valid_input(change, coins)

    if not coins:
        return 0

    coins = reversed(sorted(coins))
    count = 0

    for coin in coins:
        while change - coin >= 0:
            change -= coin
            count += 1

    return count
