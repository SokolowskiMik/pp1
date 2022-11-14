names = ['Genowefa', 'Onufry', 'celestyna', 'Alojzy', 'Pankracy']

#print(max(names))
naj = list()
for name in names:
    if len(name) > len(naj):
        naj = name
print(naj)
