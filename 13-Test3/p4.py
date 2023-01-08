cars1 = [["KR234","in"],["BA123","in"],["GX444","in"],["KR234","out"],
["BA111","in"],["BA123","out"],["KR234","in"]]

def f(d):
    cars = dict()
    for car in d:
        cars[car[0]] = car[1]
    lst = []
    for c in cars:
        if cars.get(c) == 'in':
            lst.append(c)
    return sorted(lst)

print(f(cars1))