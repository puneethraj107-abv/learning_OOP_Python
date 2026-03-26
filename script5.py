#static vs instance method example

class BankAccount:
    MIN_BALANCE=100

    def __init__(self,owner,balance=0):
        self.owner=owner
        self._balance=balance

    def deposit(self,amount):
        if amount>0:
            self._balance+=amount
            print(f'{self.owner} has {self._balance} ruppees into the account')
        else:
            print(f'you do not have the minimum amount required to make a deposit')

    @staticmethod
    def is_valid_interest_rate(rate):
        return 0<=rate<=5

bankaccount1=BankAccount('puneeth',1000)

bankaccount1.deposit(1000)
print(bankaccount1.is_valid_interest_rate(3))
print(BankAccount.is_valid_interest_rate(10))