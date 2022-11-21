f = open('.\\07-FileHandling\\numbers.txt', 'r')

suma = 0
for line in f:
    print(line.rstrip())
    suma += int(line)

f.close()   
print(suma)
