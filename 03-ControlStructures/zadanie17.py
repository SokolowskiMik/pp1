x = int(input('Type your x coordinate: '))
y = int(input('Type your y coordinate: '))

if x > 0 and y > 0:
    print(f'Point P({x},{y}) is in the first quadrant')
elif x < 0 and y > 0:
    print(f'Point P({x},{y}) is in the second quadrant')
elif x < 0 and y < 0:
    print(f'Point P({x},{y}) is in the third quadrant')
elif x==0 and y==0:
    print(f'Point P({x},{y}) is in the position (0,0) of the coordinate system')
elif x==0:
    print(f'Point P({x},{y}) is located on the y axis')
elif y==0:
    print(f'Point P({x},{y}) is located on the x axis')
else:
    print(f'Point P({x},{y}) is in the fourth quadrant')