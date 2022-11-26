array = [[7,3,7,9,0], [2,9,0,1,5],[3,8,6,4,7],[8,7,1,1,5]]

def calculate(arr):
    suma = 0
    for li in arr:
        suma += li[(len(li)-1)]
    return suma

print(calculate(array))
