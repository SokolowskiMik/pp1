file = open('.\\07-FileHandling\\countries.txt', 'r', encoding='utf-8')
i = 0
for line in file:
    i += 1
    print(i, line, end="")

file.close()
