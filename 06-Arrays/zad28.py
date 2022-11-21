arra = [1,0,9,4,6]
arrb = [6,8,3,1,0,5,7]

def bubblesort(arr):
    n = len(arr)
    for j in range(n-1):
        for i in range(n-j-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
            else:
                pass
    return arr

def median(array):
    if len(array) % 2 != 0:
        return array[(len(array)//2)]
    else:
        return ((array(len(array)//2)+(array(len(array)//2)-1))/2)

bubblesort(arra)
bubblesort(arrb)

print(arra)
print(median(arra))
print()
print(arrb)
print(median(arrb))