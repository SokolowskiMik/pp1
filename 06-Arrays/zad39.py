array = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],]

for i in range(1,(len(array)+1)):
    for j in range(len(array[i-1])):
        k = j + 1
        array[i-1][j] = i * k

for li in array:
    print(li)