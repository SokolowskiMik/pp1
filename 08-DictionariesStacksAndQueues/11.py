import json

with open("08-DictionariesStacksAndQueues\\data.json") as file:
    data = json.load(file)

for dic in data:
    for k,v in dic.items():
        print(k,":", v)