arr = [15,8,31,47,2,19]

def ar_mean(array):
    suma = 0
    for i in array:
        suma += i
    mean = suma/len(array)
    return mean

print(ar_mean(arr))