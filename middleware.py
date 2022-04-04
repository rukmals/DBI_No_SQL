import operations
import json
from blockchain.blockchain import Blockchain
from blockchain.transaction import Transaction,TransactionEncoder

blockchain =  Blockchain()

def add_transaction(request_data):
    #request_data = request.get_json()
    transaction = Transaction(request_data['id'],request_data['userID'],request_data['timestamp'],request_data['data'])
    blockchain.add_new_transaction(TransactionEncoder().encode(transaction))
    return "True"

def get_chain():
    chain_data = []
    for block in blockchain.chain:
        chain_data.append(block.__dict__)
    return json.dumps({"length": len(chain_data),
                       "chain": chain_data})
def mine():
    blockchain.mine()
    return "True"

def update(req_data):
    trans = add_transaction(req_data)
    if trans == "True":
        operations.update(req_data)
        print(mine())
        print(get_chain())
        return "Successful!"

    else:
        return "Unsucessful!"

def insert(req_data):
    trans = add_transaction(req_data)
    if trans == "True":
        operations.insert(req_data)
        print(mine())
        print(get_chain())
        return "Successful!"
    else:
        return "Unsucessful!"