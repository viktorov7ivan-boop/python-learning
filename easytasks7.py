class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        print(f"Создан счет. Начальный баланс: {balance} единиц")

    def deposit(self, balance):
        self.balance = self.balance + balance
        print(f"На счете: {self.balance} единиц")

    def withdraw(self, balance):
        if self.balance >= balance:
                    self.balance = self.balance - balance
                    print(f"На счете {self.balance} единиц")
                
        else:
            print("Не достаточно средств")
account = BankAccount("Иван", 1000)
account.deposit(500)
account.withdraw(300)
account.withdraw(1500)
        
