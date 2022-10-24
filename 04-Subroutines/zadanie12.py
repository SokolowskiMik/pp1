N = int(input('input a natural number: '))

def sum(N):
    suma = 0
    for i in range(N):
        suma = i+1 + suma
    return suma

print(sum(N))

