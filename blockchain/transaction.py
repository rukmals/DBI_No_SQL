import json
from json import JSONEncoder

class Transaction:
    """
    Transaction: a class that represents a transaction.
    """
    def __init__(self, id, userID,timestamp,data):
        self.id = id
        self.userID = userID
        self.timestamp = timestamp
        self.data = data

class TransactionEncoder(JSONEncoder):
        def default(self, o):
            return o.__dict__