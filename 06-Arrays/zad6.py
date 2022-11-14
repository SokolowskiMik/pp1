arr = [2,3,6,5,4]

print(arr)
print(len(arr))
print(arr[0])
print(arr[1])
print(arr[-1])
print(arr[-2])
print(arr[0] + arr[-1])
print(arr[len(arr)//2])
for i in arr:
    print(i, end=' ')
print()
arr2 = arr[:(len(arr)//2)+1]
for j in arr2:
    print(j, end=" ")

