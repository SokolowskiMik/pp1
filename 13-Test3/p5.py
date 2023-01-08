class C():
    def __init__(self, arr):
        self.arr = arr
        
    def __str__(self):
        s = "=" + str(sum([int(i) for i in self.arr]))
        r = "+".join([str(i) for i in self.arr])
        return r + s

c1 = C([5,12])
c2 = C([6,0,15])
print(c1)
print(c2)