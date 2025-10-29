class InsuffucientFundsError(Exception):
    pass
    
class BankAccount:
    acc_counter = 100

    def __init__(self,balance,name):
        BankAccount.acc_counter += 1
        self.name = name
        self.__balance = balance
        self.__acc = BankAccount.acc_counter

    def deposit(self,amount):
        self.__balance += amount
        
    def withdraw(self,amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            raise InsuffucientFundsError("Not enough funds")
    
    def get_balance(self):
        return self.__balance
    
    
    def details(self):
        return self.__acc, self.name , self.__balance
    
james = BankAccount('James',1000) 
ashok = BankAccount("Ashok",10000)
print(james.details())