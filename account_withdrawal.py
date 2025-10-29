class InsufficientFundsError(Exception):
    pass

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError("Not enough funds")
    return balance - amount
        
balance = 5000
amount = int(input("Enter the amount: "))

try:
    balance = withdraw(balance, amount)
    print("Withdraw is successfull")
    print("Remaining balance",balance)
except InsufficientFundsError as e:
    print(e)