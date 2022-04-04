# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import middleware
import operations
from threading import Thread
# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # y = {"id": "1",
    #      "userID": "rukmals",
    #      "timestamp": operations.get_time(),
    #      "data":{
    #                 "name":"Rukmal1",
    #                 "balance":"$500"
    #             }
    #      }

    #print(middleware.update(y))

    threads = []
    for i in range(1,101):
        y = {"id": str(i),
             "userID": "rukmals",
             "timestamp": operations.get_time(),
             "data": {
                 "name": "Rukmal1",
                 "balance": "$500"
             }
            }
        print(middleware.insert(y))
        # We start one thread per url present.
        # print(i)
        #process = Thread(target=middleware.insert, args=[y])
        #process.start()
        #process.join()
        # threads.append(process)

    # for process in threads:
    #     process.join()
    for i in range(101):
        y = {"id": str(i),
             "userID": "rukmals",
             "timestamp": operations.get_time(),
             "data": {
                 "name": "Rukmal"+str(i),
                 "balance": "$50"+str(i)
             }
            }
        print(middleware.update(y))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
