f = open('.\\07-FileHandling\\shopping.txt','a',encoding='utf-8')

while True:
    produkt = input("Podaj kolejny produkt (wpisz 'koniec' by wyjsc): ")
    if produkt == 'koniec':
        print('koniec')
        break
    else:
        f.write(str(produkt))
        f.write('\n')

f.close()
