import json
import re

def f(age,course,average):
    with open('test.json', 'r', encoding='UTF-8') as jf:
        data = json.load(jf)
    count = 0
    for i in range(len(data)):
        if data[i]["age"] >= age:
            for j in range(len(data[i]["studies"]["courses"])):
                if data[i]["studies"]["courses"][j]["name"] == course:
                    suma = sum(data[i]["studies"]["courses"][j]["grades"])
                    avg = suma // len(data[i]["studies"]["courses"][j]["grades"])
                    if avg >= average:
                        count += 1
                else: continue
        else: continue
    return count

print(f(21,"statistics",4))
