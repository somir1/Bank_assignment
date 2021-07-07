
class Bankaccount:
    def __init__(self, interest_rate, amount):
        self.interest_rate = interest_rate
        self.amount = amount

    def Deposit(self, amount):
        self.amount += amount
        print(f"You have deposited {amount}")
        return self

    def withdrawal(self, amount):
        self.amount -= amount
        print(f"You have Withdrew {amount}")
        if self.amount < 0:
            self.amount -= 5
            print('Charging a 5 dollar Fee')


        return self

    def display_user_balance(self):
        print(f"Your new balance is: {self.amount}")
        return self

    def yield_interest(self):
        self.amount += self.interest_rate * self.amount
        #100 += 0.01 * 100
        return self

class User:
    def __init__(self, userName):
        self.userName = userName
        self.Bank = Bankaccount(interest_rate = 0.01, amount = 98)

    def make_deposit(self, amount):
        self.Bank.Deposit(amount)
        return self

    def make_withdrawal(self, amount):
        self.Bank.withdrawal(self, amount)
        return self

    def show_balance(self):
        self.Bank.display_user_balance()
        return self

account1 = User('Samir')
account1.make_deposit(65).make_deposit(805).show_balance()