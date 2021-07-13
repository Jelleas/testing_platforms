def number_of_coins(change, coins):
    def integer_division(change, coin):
        if coin > change:
            return 0

        count = 1
        coin_amount = coin
        while change >= coin_amount:
            coin_amount *= 10
            count *= 10

        while change <= coin_amount:
            coin_amount -= coin
            count -= 1

        return count

    count = 0
    for coin in coins:
        if integer_division(change, coin) > 0:
            count += integer_division(change, coin)
            change = change % coin
    return count
