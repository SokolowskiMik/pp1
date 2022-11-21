arr = [5,1,9,6,1]

n = len(arr)

for j in range(n-1):
    for i in range(n-j-1):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
        else:
            pass
        
print(arr)
print(arr[-2])