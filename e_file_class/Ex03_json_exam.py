# Ex03_json_exam.py


#data / sample.json 파일을 읽고 총합 구해서 출력

f = open('./data/sample.json', 'rt', encoding='utf-8')
data = f.read()
f.close()

print(data)
print(type(data))

import json
items = json.loads(data)

for k,val in items.items():
    print(k)
    print(val['price'] * val['count'])
