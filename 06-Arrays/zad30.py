def minmax(array):
    result = []
    result.append(min(array))
    result.append(max(array))
    return result

def bubbleminmax(arra):
    n = len(arra)
    for j in range(n-1):
        for i in range(n-j-1):
            if arra[i] > arra[i+1]:
                arra[i], arra[i+1] = arra[i+1], arra[i]
            else:
                pass
        return (arra[0], arra[-1])

def bubble(ar):
    m = len(ar)
    for k in range(m-1):
        for l in range(m-k-1):
            if ar[l] > ar[l+1]:
                ar[l], ar[l+1] = ar[l+1], ar[l]
            else: pass
    return ar


arr = [4,2,8,4,7,9,5]

print('array: ', arr)
print('result: ', minmax(arr))
print('bubbleresult: ',bubbleminmax(arr))
print(bubble(arr))
arr.sort()
print(arr)