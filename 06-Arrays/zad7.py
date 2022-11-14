arr = [1,2,3,4,5]
#a.
arr[0] -= 1
print(arr[0])

#b.
arr[-1] += 4
print(arr[-1])

#c
arr[len(arr)//2] *= 2
print(arr[len(arr)//2])

#d
print()
for i in arr:
    print(i + 3, end=" ")