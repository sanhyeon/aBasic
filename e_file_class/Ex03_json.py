# Ex03_json.py

f = open('./data/temp.json', 'rt', encoding='utf-8')
data = f.read()
f.close()

print(data)
print(type(data))

import json
items = json.loads(data)

print(items)

for k,val in items.items():
    print(k, '>', val)
    print(k, '>>', val['Job'])