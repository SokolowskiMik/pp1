def create_2d_arr(x,y):
    arr = []
    for j in range(x):
        arr.append([])
        for i in range(y):
            arr[j].append('0')
    return arr

print(create_2d_arr(3,5))