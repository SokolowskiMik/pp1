import re

text = "To be, or not to be, that is the question"

def find_vowels(txt):
    vowels = re.findall('([aeyiuo]+?)', txt)
    return (vowels, len(vowels))

print(find_vowels(text))
