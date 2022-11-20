arr = [12,6,4,9,10]

def star(n):
    return (n * '*')

def go(array):
    for i in array:
        print(f'{i}: ', star(i))

go(arr)