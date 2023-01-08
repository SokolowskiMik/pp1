import re
def f1(t):
    names = re.findall(r'[A-Z][a-z]+',t)
    ages = re.findall(r'\d+',t)

    d = dict()
    i = 0
    for name in names:
        if name not in d:
            d[name] = ages[i]
            i += 1
    return dict(sorted(d.items()))

def f2(t):
    ages = re.findall(r'\d+',t)
    return sum(int(age) for age in ages)
print(f1("Mark is 24 and Ann is 27"))
print(f1("Peter is 11, Barbara is 7 and their grandfather John is 103!!"))

print(f2("Mark is 24 and Ann is 27"))
print(f2("Peter is 11, Barbara is 7 and their grandfather John is 103!!"))

        