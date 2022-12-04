import re

with open('grades.txt', 'r', encoding='UTF-8') as fhand:
    for line in fhand:
        line = line.rstrip()
        if line.startswith("Name: "):
            name = re.findall('^Name: ([a-zA-Z]+)', line)
            print(name, end=': ')
        elif line.startswith('Grades: '):
            grades = re.findall('([0-9.]+)', line)
            print(grades)
            suma = 0
            for grade in grades:
                suma += float(grade)
            print(round(suma/len(grades),4))
        else: continue



