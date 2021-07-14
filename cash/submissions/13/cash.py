def number_of_coins(change, coins):
    if any(isinstance(number, float) for number in [change] + coins):
        raise TypeError

    if any(coin <= 0 for coin in coins) or change < 0:
        raise ValueError

    coins = sorted(coins)[::-1]

    return number_of_coins_helper(change, coins)

def number_of_coins_helper(change, coins):
    if len(coins) == 1:
        return change // coins[0]

    return change // coins[0] + number_of_coins(change % coins[0], coins[1:])
