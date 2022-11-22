#bubble sort ale dla modulo

array = [1,2,3,4,5,6,7,8,9]

def evenodd(arr):
    a = len(arr)
    for j in range(a-1):
        for i in range(a-1):
            if arr[i] % 2 != 0 and arr[i+1] % 2 == 0:
                arr[i], arr[i+1] = arr[i+1], arr[i]
            else:
                pass
    return(arr)

print(evenodd(array))
