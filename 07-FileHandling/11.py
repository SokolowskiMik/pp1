film_titles = ["Pasja","zielona mila", "300", "Joker", "kogelmogel"]

f = open('.\\07-FileHandling\\films.txt', 'w', encoding='utf-8')

for film in film_titles:
    f.write(film)
    f.write('\n')

f.close()