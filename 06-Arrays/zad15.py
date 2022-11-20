arr = [[0,0,0],[0,0,0],[0,0,0]]

def replace(array):
    i = 0
    for li in array:
        for val in li:
            li[i] = 1  
        i += 1
    return array

print(replace(arr))
