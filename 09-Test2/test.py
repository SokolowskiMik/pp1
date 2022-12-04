import csv
import json

with open('test.csv', 'r', encoding='UTF-8') as csvf:
    c = csv.reader(csvf)
    datac = list(c)
print(type(c))
print(datac)
with open('test.json', 'r', encoding='UTF-8') as jf:
    j = json.load(jf)
print(type(j))
with open('test.txt', 'r', encoding='UTF-8') as tf:
    t = tf.read()
print(type(t))