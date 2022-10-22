from tkinter import Y


a = 5
b = 2
c = 1
suma = 0
amount = int(input('Input any natural number: '))

x = amount // 5
y = (amount - x*5) // 2
z = (amount - (x*5 + y*2)) // 1

print(f'The amount of PLN {amount} in coins: \n', f'5 zł - {x} \n', f'2 zł - {y} \n', f'1 zł - {z} \n')


