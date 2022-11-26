array = [[1,2,3,4,5],
         [6,7,8,9,10],
         [11,12,13,14,15]]

for row in array:
    print(row)

for rw in array:
    if array.index(rw) == 0:
        addi = array[0]
        array[0] = array[(len(array))-1]
        array[(len(array))-1] = addi
    else:
        pass
# array.reverse()
print()

for r in array:
    print(r)

