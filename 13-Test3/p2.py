def f(arr):
    k = 1
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] != arr[0][j] * k:
                return False
        k += 1
    return True

print(f([[1,2,3],[2,4,6],[3,6,9]]))
print(f([[1,2],[2,4]]))
print(f([[1,2,3,4],[2,4,6,8],[3,6,9,12],[4,8,12,16]]))
print(f([[1,2],[3,6]]))
print(f([[1,2,3],[2,4,6]]))
print(f([[1,2,3],[2,5,6]]))