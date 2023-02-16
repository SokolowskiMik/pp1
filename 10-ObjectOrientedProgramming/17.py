class Stat():
    def __init__(self):
        self.arr = []

    def add(self, number):
        self.arr.append(number)
    
    def display(self):
        for i in self.arr:
            print(i, end=' ')
        print()
    
    def smallest(self):
        print(min(self.arr))

    def greatest(self):
        print(max(self.arr))

    def a_m(self):
        am = sum(self.arr)/len(self.arr)
        print(f'arithmetic mean: {am}')
    
    def median(self):
        ar = sorted(self.arr)
        if len(self.arr)%2 == 0:
            m = (ar[len(ar)-1//2-1]+ar[len(ar)//2])/2
        else:
            m = ar[len(self.arr)//2]
        print(f'median: {m}')

a1 = Stat()
a1.add(12)
a1.add(37)
a1.add(6)
a1.add(9)
a1.add(17)
a1.display()
a1.smallest()
a1.greatest()
a1.a_m()
a1.median()

    
    
