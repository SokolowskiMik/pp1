import re

def f(first_letter,last_letter):
    with open('test.txt', 'r', encoding='UTF-8') as f:
        data =  f.read()
    
    word = re.findall(rf'\b{first_letter}\w*{last_letter}\b', data)
    return len(word)

# or

def f1(first_letter,last_letter):
    with open('test.txt', 'r', encoding='UTF-8') as f:
        data =  f.read()
    
    word = re.findall(rf'\b{first_letter}\S*{last_letter}\b', data)
    return len(word)

print(f('w','d')) 
print(f1('w','d'))     
    