class C():
    @staticmethod
    def m1(n):
        new_n = ''
        s = str(n)
        for dig in s:
            if int(dig)  % 2 == 0:
                new_n += dig
            else: continue
        return int(new_n)

    @staticmethod
    def m2(n):
        s = str(n)
        j = 1
        for i in range(len(s)-1):
            if s[i] <= s[j]:
                j+=1
                continue
            else:
                return False
        return True

    @staticmethod
    def m3(n):
        return "".join([str(i) for i in [0,1,2,3,4,5,6,7,8,9] if str(i) not in str(n)])


print(C.m1(4231564))
print(C.m1(79381))
print(C.m2(125579))
print(C.m2(4557879))
print(C.m3(23557))
print(C.m3(12340))