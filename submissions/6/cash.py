def assert_valid_input(change, coins):
    if any(isinstance(number, float) for number in [change] + coins):
        raise TypeError

    if any(coin == 0 for coin in coins) or change < 0:
        raise ValueError

def map_and_reduce(func, iterable, initial):
    results = []
    for value in iterable:
        prev_result = results[-1] if results else initial
        result = func(prev_result, value)
        results.append(result)
    return results

def number_of_coins(change, coins):
    assert_valid_input(change, coins)
    coins = sorted(coins)[::-1]
    changes = map_and_reduce(lambda a, b: a % b, coins, change)
    changes = [change] + changes[:-1]
    counts = map(lambda change_and_coin: change_and_coin[0] // change_and_coin[1], zip(changes, coins))
    return sum(counts)