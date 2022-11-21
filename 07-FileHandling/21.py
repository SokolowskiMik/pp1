f = open(".\\07-FileHandling\\powers.txt", 'a')

for i in range(1,11):
    f.write(f'{str(i)}, {str(i**2)}, {str(i**3)}')
    f.write('\n')