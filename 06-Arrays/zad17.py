arr = [8,2,5,1,9]

def square_power(array):
    for i in range(len(array)):
        arr[i] = arr[i] ** 2
    return arr

print(square_power(arr))