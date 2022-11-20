arr1 = [4,36,12,28,9,44,5]
arr2 = [5,1,36]

def check(a1,a2):
    for val in a1:
        for value in a2:
            if val == value:
                break
        else:
            print(val)

check(arr1,arr2)