
class BankAccount:
    def __init__(self, number, balance=0):
        self.balance = balance
        self.number = number

    def withdraw(self, amount):
        self.balance -= amount

# Define __eq__ that returns True if the number attributes and their types are equal
    def __eq__(self, other):
        return (self.number == other.number) and (type(self) == type(other))

class Phone:
  def __init__(self, number):
     self.number = number

  def __eq__(self, other):
    return self.number == \
          other.number

# Create accounts and compare them
acct1 = BankAccount(123, 1000)
acct2 = BankAccount(123, 1000)
acct3 = BankAccount(456, 1000)
print(acct1 == acct2)
print(acct1 == acct3)
print()
# Create phone number and compare with accounts
acct = BankAccount(873555333)
pn = Phone(873555333)
print(acct == pn)
