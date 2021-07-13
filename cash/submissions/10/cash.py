from typing import Type


class State:
    def __init__(self, change, coins, count=0):
        self.change = change
        self.coins = coins
        self.count = count

    def create(self, state_type):
        return state_type(self.change, self.coins, self.count)

class StartState(State):
    def run(self):
        pass

    def next(self):
        return self.create(ValidationState)

class ValidationState(State):
    def run(self):
        if any(isinstance(coin, float) for coin in self.coins):
            raise TypeError

        if any(coin <= 0 for coin in self.coins) or self.change < 0:
            raise ValueError

    def next(self):
        return self.create(CorrectionState)

class CorrectionState(State):
    def run(self):
        self.coins = sorted(self.coins)
        self.coins = self.coins[::-1]

    def next(self):
        if not self.coins:   
            return self.create(EndState)
        return self.create(CountState)

class CountState(State):
    def run(self):
        self.count += self.change // self.coins[0]

    def next(self):
        return self.create(ChangeState)

class ChangeState(State):
    def run(self):
        self.change %= self.coins[0]

    def next(self):
        return self.create(CoinState)

class CoinState(State):
    def run(self):
        self.coins.pop(0)

    def next(self):
        if not self.coins:
            return self.create(EndState)
        return self.create(CountState)

class EndState(State):
    def run(self):
        pass

    def next(self):
        return self

def number_of_coins(change, coins):
    state = StartState(change, coins)

    while not isinstance(state, EndState):
        state.run()
        state = state.next()

    return state.count

print(number_of_coins(45, [25,10,5,1]))