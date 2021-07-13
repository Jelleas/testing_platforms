def assert_valid_input(change, coins):
    if any(isinstance(number, float) for number in [change] + coins):
        raise TypeError

    if any(coin < 0 for coin in coins) or change < 0:
        raise ValueError

    return change, coins

def fix_input(change, coins):
    coins = sorted(coins)[::-1]
    return change, coins

def calculate_coins(change, coins):
    if not coins:
        return 0

    coin, coins = coins[0], coins[1:]
    n_coins = change // coin
    change = change % coin
    
    return n_coins + calculate_coins(change, coins)

def number_of_coins(change, coins):
    return calculate_coins(*fix_input(*assert_valid_input(change, coins)))