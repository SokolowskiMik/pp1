def f(player1, player2):
    cards = {
        'A': 10,
        'K': 10,
        'Q': 10,
        'J': 10,
        'T': 10,
        '9': 9,
        '8': 8,
        '7': 7,
        '6': 6,
        '5': 5,
        '4': 4,
        '3': 3,
        '2': 2,
        '1': 1,
        '0': 0
    }
    count1 = 0
    count2 = 0
    for card in player1:
        count1 += cards.get(card)
    for card in player2:
        count2 += cards.get(card)

    if count1 > count2:
        return True
    else:
        return False

print(f("AJ972","AQT72"))
print(f("9532", "K8"))
print(f("987","AT4"))


