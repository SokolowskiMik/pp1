arr = [
        [1,1,1,1,8],
        [2,2,2,2,9],
        [3,4,5,6,7]
        ]

for i in arr:
    print(i)
print()
i = 0
for row in arr:
    j=0
    for col in row:
        if row.index(col) == 0:
            arr[i][j], arr[arr.index(row)][len(row)-1] = arr[arr.index(row)][len(row)-1], arr[i][j]
        else: pass
        j += 1
    i += 1
        

for x in arr:
    print(x)    


    


