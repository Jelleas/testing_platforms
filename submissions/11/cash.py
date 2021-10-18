import collections

class Event(Exception):
    pass

class ValidationEvent(Event):
    pass

class CorrectionEvent(Event):
    pass

class CalculationEvent(Event):
    pass

class Registry:
    def __init__(self):
        self.callbacks = collections.defaultdict(list)

    def register(self, event, callback):
        self.callbacks[event].append(callback)

    def fire(self, event):
        for callback in self.callbacks[event]:
            callback()

    def run(self, start_event):
        event = start_event
        while event:
            try:
                self.fire(event)
            except Event as e:
                event = type(e)
            else:
                return

def number_of_coins(change, coins):
    count = 0

    def validation():
        if any(isinstance(val, float) for val in coins + [change]):
            raise TypeError

        if any(coin <= 0 for coin in coins) or change < 0:
            raise ValueError

        raise CorrectionEvent

    def correction():
        nonlocal coins
        coins = sorted(coins)[::-1]
        raise CalculationEvent

    def calculation():
        nonlocal change, coins, count

        if not coins:
            return

        coin = coins.pop(0)
        count += change // coin
        change %= coin
        raise CalculationEvent

    registry = Registry()
    registry.register(ValidationEvent, validation)
    registry.register(CorrectionEvent, correction)
    registry.register(CalculationEvent, calculation)

    registry.run(ValidationEvent)
    
    return count