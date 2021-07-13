def number_of_coins(change, coins):
    count = 0
    for coin in coins:
        while change - coin > 0:
            change -= coin
            count += 1
    return count