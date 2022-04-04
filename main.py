# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import middleware
import operations
# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    y = {"id": "1",
         "userID": "rukmals",
         "timestamp": operations.get_time(),
         "data":{
                    "name":"Rukmal1",
                    "balance":"$500"
                }
         }

    print(middleware.update(y))
    #search_item = transaction.update(y)
    #operations.update(y)
    #operations.insert(y)
    #print(search_item)
    #print(search_item)




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
