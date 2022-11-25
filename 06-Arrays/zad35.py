import random

def rand_elem(array):
    x = random.randrange(len(array))
    return(array[x])

arr = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

print(rand_elem(arr))