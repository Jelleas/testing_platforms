def number_of_coins(change, coins):
    count = 0
    for coin in coins:
        if change // coin > 0:
            change //= coin
            count += change % coin
    return count
