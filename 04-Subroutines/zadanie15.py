import mymath

x = mymath.generate_number()
print('correct answer:', x)
y = mymath.read_number()

if y == x:
    print('You won')
        
else:
    print('you lose')
        
