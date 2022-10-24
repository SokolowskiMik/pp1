def  keypad():
    for i in range(1, 10, 3):
        for j in range(3):
            print(i+j, end=" ")
        print()

keypad()