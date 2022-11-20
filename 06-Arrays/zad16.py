arr = [15,8,31,47,2,19]

def reversed(ar):
    arr.reverse()
    return arr

print(reversed(arr))


#albo
arr = [15,8,31,47,2,19]

def reversed2(ar2):
    new = []
    for i in range((len(ar2)-1),-1,-1):
        new.append(ar2[i])
    return new

print(reversed2(arr))