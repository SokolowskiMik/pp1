arr = [[True,False],[True,True],[False,False]]

def change(array):
    i = 0
    
    for li in array:
        j = 0
        for value in li:
            if value == True:
                array[i][j] = False
                j += 1
            else:
                array[i][j] = True
                j += 1
        i += 1
    return(array)

print(change(arr))