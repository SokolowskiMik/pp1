f1 = open('MeatAndFish.txt', 'r', encoding='UTF-8')
f2 = open('GrainsAndBread.txt', 'r', encoding='UTF-8')
fs = open('shoppinglist.txt', 'a', encoding='UTF-8')

fs.write(f1.read())
fs.write(f2.read())
f1.close()
f2.close()
fs.close()