arr = [12,1,6,23,234,456,2,35,687,34]

n = len(arr)

def bublesort(array):
    for j in range(n-1):
        for i in range(n-j-1):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
            else:
                pass
    return array

print(bublesort(arr))