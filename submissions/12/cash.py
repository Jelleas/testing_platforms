import uuid

class Server:
    def __init__(self):
        self.database = {}

        def coins_constraint(coins):
            if any(isinstance(coin, float) for coin in coins):
                raise TypeError

            if any(coin <= 0 for coin in coins):
                raise ValueError

            return sorted(coins)[::-1]

        def change_constraint(change):
            if isinstance(change, float):
                raise TypeError

            if change < 0:
                raise ValueError

            return change

        self.constraints = {
            "change": change_constraint,
            "coins": coins_constraint,
            "count": lambda x : x
        }

    def on_new_connection(self, connection_id):
        self.database[connection_id] = {
            "change": 0,
            "coins": [],
            "count": 0
        }

    def is_accepting_connections(self):
        return True

    def get(self, connection_id, key):
        return self.database[connection_id][key]

    def put(self, connection_id, key, value):
        self.database[connection_id][key] = self.constraints[key](value)


class Operator:
    def __init__(self, servers):
        self.servers = servers
        self.connections = {}
        self.clients = {}

    def connect(self, client):
        if client in self.clients:
            open_connections = self.clients[client]
            if open_connections:
                return open_connections[0]
        else:
            self.clients[client] = []

        for server in self.servers:
            if server.is_accepting_connections():
                connection_id = uuid.uuid4()

                self.connections[connection_id] = server
                self.clients[client].append(connection_id)

                server.on_new_connection(connection_id)

                return connection_id

    def handle_request(self, connection_id, request, *params):
        server = self.connections[connection_id]
        handler = getattr(server, request)
        return handler(connection_id, *params)


OPERATOR = Operator([Server(), Server(), Server()])

def number_of_coins(change, coins, login="admin"):
    connection_id = OPERATOR.connect(login)

    OPERATOR.handle_request(connection_id, "put", "change", change)
    OPERATOR.handle_request(connection_id, "put", "coins", coins)

    coins = OPERATOR.handle_request(connection_id, "get", "coins")
    change = OPERATOR.handle_request(connection_id, "get", "change")
    count = OPERATOR.handle_request(connection_id, "get", "count")

    while coins:
        coin = coins.pop(0)
        count += change // coin
        change %= coin

        OPERATOR.handle_request(connection_id, "put", "change", change)
        OPERATOR.handle_request(connection_id, "put", "count", count)

        change = OPERATOR.handle_request(connection_id, "get", "change")
        count = OPERATOR.handle_request(connection_id, "get", "count")

    return count