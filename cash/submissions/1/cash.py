def number_of_coins(change, coins):
    count = 0
    for coin in coins:
        change -= coin
        count += 1
    return count