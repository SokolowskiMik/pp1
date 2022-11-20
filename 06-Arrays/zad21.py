arr11 = ["water","book","sky"] 
arr12 =  ["water","book","sky"]
arr21 = [True,False] 
arr22 =  [True,False,True]
arr31 = [5,3,1] 
arr32 =  [5,3,1]
arr41 = [3,2,1] 
arr42 =  [3,2]

def compare(array1, array2):
    print(f'Array1: {array1}')
    print(f'Array2: {array2}')
    if len(array1) == len(array2):
        for i in range(len(array1)):
            if array1[i] == array2[i]:
                continue
            else:
                print('Comparison: arrays are not the same')
                quit()
        print('Comparison: arrays are the same')
    else:
        print('Comparision: arrays are not the same')

compare(arr11,arr12)
compare(arr21,arr22)
compare(arr31,arr32)
compare(arr41,arr42)
