class C:
    def __init__(self, d: dict):
        self.d = d

    def m(self,n):
        lst = []
        for name in self.d:
            if (sum(self.d.get(name))/len(self.d.get(name))) >= n:
                lst.append(name)
        lst = sorted(lst) 
        return ','.join(lst)

s = C({"Peter":[4,5,4], "Harry":[2,5], "Barbara":[3,3,3,5,5,5]})
print(s.m(4))
print(s.m(3))
print(s.m(5))