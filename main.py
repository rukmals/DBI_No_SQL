# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import json_hash
import operations
import json
from blockchain.blockchain import Blockchain
from blockchain.transaction import Transaction,TransactionEncoder
#def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    #print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
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
# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    y = {"id": "1",
         "userID": "rukmals",
         "timestamp": operations.get_time(),
         "data":{
                    "name":"Rukmal1",
                    "balance":"$300"
                }
         }
    print(add_transaction(y))
    #print(add_transaction(y))

    print(mine())
    print(get_chain())
    #search_item = transaction.update(y)
    #operations.update(y)
    #operations.insert(y)
    #print(search_item)
    #print(search_item)




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
