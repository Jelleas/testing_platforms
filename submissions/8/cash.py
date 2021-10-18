jobs = []
state = {}

def assert_no_floats():
    if any(isinstance(number, float) for number in [state["change"]] + state["coins"]):
        raise TypeError

def assert_no_negativity():
    if any(coin <= 0 for coin in state["coins"]) or state["change"] < 0:
        raise ValueError

def sort_coins():
    state["coins"] = sorted(state["coins"])[::-1]

def count_coins():
    state["count"] += state["change"] // state["coins"][0]
    state["change"] = state["change"] % state["coins"][0]
    state["coins"] = state["coins"][1:]

def work():
    while jobs:
        job = jobs.pop(0)
        job()

def load():
    jobs.append(assert_no_floats)
    jobs.append(assert_no_negativity)
    jobs.append(sort_coins)
    
    for _ in state["coins"]:
        jobs.append(count_coins)

def number_of_coins(change, coins):
    state["change"] = change
    state["coins"] = coins
    state["count"] = 0

    load()
    work()

    return state["count"]