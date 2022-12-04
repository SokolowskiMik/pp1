import re

text = "To be, or not to be, that is the question"

def nofwords(txt):
    txt = re.sub(',','', txt)
    words = re.findall('([a-zA-Z]+\S)', txt)
    return (words, len(words))

print(nofwords(text))