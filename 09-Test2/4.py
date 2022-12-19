
def f(dict, x, y):
    s = 0
    for key in dict:
        for number in dict[key]:
            if number in range(x, y+1):
                s += number
    return s


print(f({"arr1": [2, 6, 5], "arr2": [7, 1], "arr3": [2, 9, 8, 1]}, 5, 10))
