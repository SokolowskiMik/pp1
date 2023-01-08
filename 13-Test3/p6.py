class C():
    def __init__(self, counter: int):
        self.c = counter

    def m1(self):
        return self.c
    
    def m2(self):
        self.c += 1
    
    def m3(self):
        self.c -= 1

    def m4(self, n):
        self.n = n
        self.c += n

c=C(5)
print(c.m1())
c.m2()
print(c.m1())
c.m4(-8)
print(c.m1())
c.m3()
print(c.m1())
c.m4(10)
print(c.m1())
