import json
import hashlib

def hashing_json():
    x = '{ "name":"John", "age":30, "city":"New York"}'
    y = json.dumps(x,sort_keys=True).encode('utf8')
    print(y)
    h = hashlib.new('sha256')
    h.update(y)
    print(h.hexdigest())
