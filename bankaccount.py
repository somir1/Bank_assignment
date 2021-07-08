
class Bankaccount:
    def __init__(self, interest_rate, amount):
        self.interest_rate = interest_rate
        self.amount = amount

    def make_Deposit(self, amount):
        self.amount += amount
        print(f"You have deposited {amount}")
        return self

    def make_withdrawal(self, amount):
        self.amount -= amount
        print(f"You have Withdrew {amount}")
        if self.amount < 0:
            self.amount -= 5
            print('Charging a 5 dollar Fee')

        return self

    def display_user_balance(self):
        print(f"Your new balance is: {self.amount}")

    def yield_interest(self):
        self.amount += self.interest_rate * self.amount
        #100 += 0.01 * 100
        return self

account1 = Bankaccount(0.01, 100)
account2 = Bankaccount(0.01, 1900)
account3 = Bankaccount(0.01, 100)

account1.make_Deposit(50).make_Deposit(10).make_Deposit(100).make_withdrawal(20).yield_interest().display_user_balance()
account2.make_Deposit(30).make_Deposit(30).make_withdrawal(5).make_withdrawal(6).make_withdrawal(10).make_withdrawal(50).yield_interest().display_user_balance()
account3.make_withdrawal(100).make_withdrawal(10).yield_interest().display_user_balance()
