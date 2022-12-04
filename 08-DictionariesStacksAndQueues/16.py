import json


with open('student.json') as fjson:
    j = json.load(fjson)
limited = ["gender","email","year_of_study"]
with open('limited.json', 'w', encoding='UTF-8') as fhand:
    for i in range(len(j)):
        for key in limited:
            j[i].pop(key)
    json.dump(j, fhand, indent=4)