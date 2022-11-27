def convert(arr):
    a1d = []
    for row in arr:
        for col in row:
            a1d.append(col)
    return a1d

ma = [[2,3],[1,5]]
mb = [[5,0,3,7,5],[9,0,9,1,2]]
mc = [[2,1],[3,5],[7,4],[2,6]]

print(convert(ma))
print(convert(mb))
print(convert(mc))