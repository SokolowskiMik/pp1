from math import pi
class Area():
    @staticmethod
    def triangle(base, height):
        area = (base * height) /2
        return f'triangle area = {area}'
    def rectangle(side1, side2):
        area = side1 * side2
        return f'rectangle area = {area}'
    def circle(radius):
        area = pi * pow(radius,2)
        return f'circle area = {pow(radius,2)} * pi = {area}'

print(Area.circle(3))
print(Area.rectangle(4,7))
print(Area.triangle(6,2))