def f(array2D):
    lst = []
    n = len(array2D)
    m = len(array2D[0])
    for j in range(m):
        suma = 0
        for i in range(n):
            suma += array2D[i][j]
        lst.append(suma)
    return lst

print(f([[3,6,2,7],[9,5,4,0],[2,8,0,9]]))
