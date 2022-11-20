arr = [15,8,31,47,2,19]

def aryth(array):
    i = 0
    count = 0
    suma = 0
    while i < len(array):
        suma += array[i]
        i += 1
        count += 1
    return (suma/count)

print(aryth(arr))
