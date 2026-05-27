# Understanding OOP and Encapsulation
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return True
        return False

    def get_balance(self):
        return self.__balance

acct = BankAccount("Alice", 1000)
acct.deposit(500)
acct.withdraw(200)
print(f"Balance: ${acct.get_balance()}")
