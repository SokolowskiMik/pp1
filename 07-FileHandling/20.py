import random

file = open('.\\07-FileHandling\\random.txt','a')

i = 0
while i < 50:
    file.write(str(random.randint(100, 999)))
    file.write('\n')
    i += 1