def f(dictionary,x,y):
    suma = 0
    for key in dictionary.keys():
        vals = dictionary[key]
        for val in vals:
            if val in range(x,(y+1)):
                suma += val
    return suma

print(f({"arr1":[4,5,6],"arr2": [7,5]},5,6))
print(f({"arr1":[2,6,5],"arr2": [7,1],"arr3": [2,9,8,1]},5,10))