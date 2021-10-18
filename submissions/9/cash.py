def step_1(change, coins, count):
    if isinstance(change, float) : raise TypeError
    return step_2(change, coins, count)

def step_2(change, coins, count):
    if any(coin <= 0 for coin in coins) or change < 0: raise ValueError
    return step_3(change, coins, count)

def step_3(change, coins, count):
    coins = sorted(coins)[::-1]
    return step_4(change, coins, count)

def step_4(change, coins, count):
    if not coins: return count
    return step_5(change, coins, count)

def step_5(change, coins, count):
    count += change // coins[0]
    return step_6(change, coins, count)

def step_6(change, coins, count):
    change = change % coins[0]
    return step_7(change, coins, count)

def step_7(change, coins, count):
    coins.pop(0)
    return step_4(change, coins, count)

def number_of_coins(change, coins):
    return step_1(change, coins, 0)