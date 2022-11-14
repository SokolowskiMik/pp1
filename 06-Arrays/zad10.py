arr = [1,2,3,4,5,6,7,8,9]

i = len(arr)
even = 0
odd = 0


while i > 0:
    i -= 1
    if arr[i] % 2 == 0:
        even += 1
    else:
        odd += 1

print(even, odd)