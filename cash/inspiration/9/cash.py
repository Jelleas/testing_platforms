def number_of_coins(change, coins):
    count = 0
    for coin in coins:
        if change // coin > 0:
            count += change % coin
            change //= coin
    return count