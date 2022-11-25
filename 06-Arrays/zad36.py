arr = [[1,2,3,4],[5,6,7,8]]

def display(array):
    for i in range(2):
        for j in range(4):
            print(array[i][j], end=" ")
        print()

display(arr)