class Bank:
    def __init__(self,balance):
        self.balance = balance
        
    def deposit(self,amount):
        self.balance += amount
        print(f'Deposited {amount}. New self.balance: {self.balance}')

    def withdraw(self,amount):
        if amount > self.balance:
            print('Insufficient funds')
        else:
            self.balance -= amount
            print(f'Withdrew {amount}. New self.balance: {self.balance}')

    def check_balance(self):
        print(f'Current balance: {self.balance}')

if __name__ == '__main__':
    balance=float(input('enter your balance: '))
    b=Bank(balance)
    while True:
        choice=input('choose 1 to deposit\nchoose 2 to withdraw\nchoose 3 to check balance\n')
        if choice == '1':
            amount =  float(input('enter your amount: '))
            b.deposit(amount)
        elif choice == '2':
            amount =  float(input('enter your amount: '))
            b.withdraw(amount)
        elif choice == '3':
            b.check_balance()
        else:
            break