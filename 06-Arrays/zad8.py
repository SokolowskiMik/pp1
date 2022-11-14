arr = [-15, 8, -31, 47, -2, 19]

maks = 0
mini = 0
for i in arr:
    if i > maks:
        maks = i
    elif i < mini:
        mini = i
print(f'maks: {maks}, min: {mini}')
