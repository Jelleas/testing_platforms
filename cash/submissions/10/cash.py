def number_of_coins(change, coins):
    count = 0
    
    def exchange_coin(coin):
        nonlocal count, change
        count += change % coin
        change //= coin

    map(exchange_coin, coins)

    return count