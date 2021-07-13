def number_of_coins(change, coins):
    count = 0
    for coin in coins:
        if change // coin > 0:
            count += change % coin
            change //= coin
    return count

print(number_of_coins(45, [25, 10, 5, 1]))