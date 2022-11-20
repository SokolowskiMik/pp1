array = [2,3,2,5,8,1,9,8]
print(array)

def uni(arr):
    ue = []
    add = 0
    for num in arr:
        add += 1
        for i in range(add, len(arr)):
            if num == arr[i]:
                del arr[i]
                arr.remove(num)
                break
            else:
                pass
                
    return arr


print(uni(array))