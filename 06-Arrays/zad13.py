arr = [[3,9,2],[2,4,5],[7,1,6],[0,4,8]]

def suma(tablica):
    suma = 0
    for lista in tablica:
        for liczba in lista:
            if liczba % 2 == 0:
                suma += liczba
    return suma

print(suma(arr))
