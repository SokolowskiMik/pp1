fhand = open('loremipsum.txt', 'r', encoding='UTF-8')
fcopy = open('cpylines.txt', 'a', encoding='UTF-8')

for line in fhand.readlines():
    fcopy.write(line)
