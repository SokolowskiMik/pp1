array1 = [1,2,3,4,5,6,7,8,9]
array2 = [1,6,9,2,5,7,10,21,8]

def check(arr1,arr2):
    val = None
    if len(set(arr1)) > len(set(arr2)):
        for i in arr2:
            if val == None or val == True:
                if i in arr1:
                    val = True
                else:
                    val = False
                    break
    else:
        print('arr2 not sub to arr1')
        quit()
    if val == True:
        print('arr2 is sub to arr1')
    else:
        print('arr2 not sub to arr1')


check(array1,array2)
