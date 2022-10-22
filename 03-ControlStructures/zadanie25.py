a = int(input('Enter width: '))
b = int(input('Enter height: '))
for i in range(a):
    for j in range(b):
        if i == 0 or i == (a - 1) or j == 0 or j == (b-1):
            print('*', end="")
        else:
            print(' ', end="")
    print()

    