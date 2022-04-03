import json
import datetime


def insert(data):
    id = data['id']
    check_available = search(id)
    if check_available ==None:
        with open("database/db.json",'r+') as file:
            file_data = json.load(file)
            file_data["documents"].append(data)
            file.seek(0)
            json.dump(file_data, file, indent = 4)
        print("Successfully Inserted!")

def search(id):
    obj = json.load(open("database/db.json"))
    documents = obj['documents']
    search_item = None
    for i in range(len(documents)):
        if documents[i]['id']==id:
            print("found!")
            search_item = documents[i]
            break
    return search_item

def update(data):
    obj = json.load(open("database/db.json"))
    documents = obj['documents']
    id = data['id']
    data_keys = dict(data).keys()
    for i in range(len(documents)):
        if documents[i]['id'] == id:
            write_db_ledger(data)
            for key in data_keys:
                if documents[i][key]!=None:
                    obj['documents'][i][key] = data[key]

    open("database/db.json", "w").write(json.dumps(obj, sort_keys=True, indent=4, separators=(',', ': ')))

def write_db_ledger(data):
    obj = json.load(open("database/db.json"))
    documents = obj['documents']
    id = data['id']
    new_data = None

    if id==None:
        print("update can not be proceed!")
    else:
        searched_data = search(id)
        if searched_data != None:
            with open("database/db_ledger.json", 'r+') as file:
                file_data = json.load(file)
                new_data = data
                new_data["commit_time"] = get_time()
                new_data["user"] = get_user()
                file_data["documents"].append(new_data)
                file.seek(0)
                json.dump(file_data, file, indent=4)

    print(new_data)

def get_time():
    commit_time = datetime.datetime.now()
    #print(str(commit_time))
    return str(commit_time)

def get_user():
    user_name = "rukmals"
    return user_name

