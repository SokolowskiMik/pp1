import re

with open('loremipsum.txt', 'r', encoding='UTF-8') as fhand:
    text = fhand.read()
    words = re.findall('[a-zA-Z]{6}[a-zA-Z]*', text)
    for word in words:
        print(word)