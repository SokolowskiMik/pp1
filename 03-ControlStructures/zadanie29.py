from re import I


quantity = 0
suma = 0
mean = 0
i = 1
while True:
    num = int(input('Enter a number: '))
    if num == 0:
        break
    else:
        suma = suma + num
        mean = suma / i
        i += 1
        quantity += 1
    
print(f'RESULT: Quantity={quantity}, Sum={suma}, Mean={mean}')