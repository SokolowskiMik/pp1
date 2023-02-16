class Ba():

    def __init__(self,a_number: str, a_owner_name, a_owner_surname):
        self.number = a_number
        self.name = a_owner_name
        self.surname = a_owner_surname
        self.balance = 0

    def db(self):
        print(f"Your current balance: {self.balance} PLN")

    def deposit(self, ammount):
        self.balance += round(ammount,2)
        self.balance = round(self.balance,2)

    def withdraw(self, ammount):
        self.balance -= round(ammount,2)
        self.balance = round(self.balance,2)

a1 = Ba('12 3456 5555 9090 1111 0000 7722', 'mike', 'wazowski')
a1.db()
a1.deposit(25.30)
a1.db()
a1.withdraw(31.70)
a1.db()
a1.deposit(14)
a1.db()