arr = [[-38,19],[5,40],[-7,11],[29,16]]

mi = 0
ma = 0
posmi = None
posma = None
posmi2 = None
posma2 = None
for li in arr:
    for arg in li:
        if arg > ma:
            ma = arg
            posma = li.index(arg)
            posma2 = arr.index(li)
        elif arg < mi:
            mi = arg
            posmi = li.index(arg)
            posmi2 = arr.index(li)
        else: pass  

print(mi, f'({posmi2}.{posmi})')
print(ma, f'({posma2},{posma})')

