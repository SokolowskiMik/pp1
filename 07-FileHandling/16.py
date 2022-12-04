fhand = open('loremipsum.txt', 'r', encoding="UTF-8")
fcopy = open('copy.txt', 'a', encoding='UTF-8')

fcopy.write(fhand.read())
fhand.close()
fcopy.close()