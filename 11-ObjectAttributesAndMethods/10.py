import math

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __str__(self):
        return f'P({self.x},{self.y})'
    def __eq__(self,other):
        if isinstance(other,Point):
            dist1 = self.x - other.x
            dist2 = self.y - other.y
            dist = dist1+dist2
            if dist == 0:
                return f'the distance between them is {dist}'
            else:
                dist = math.sqrt(pow(self.x-other.x,2)+pow(self.y-other.y, 2))
                return f'the distance between them is {dist}'

p1 = Point(5,5)
p2 = Point(5,5)
p3 = Point(2,2)

print(p1 == p2)
print(p1 == p3)