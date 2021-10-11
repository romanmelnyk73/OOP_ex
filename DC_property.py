class Customer:
    def __init__(self, name, new_bal):
        self.name = name
        if new_bal < 0:
            raise ValueError("Invalid balance")
        else:
            self._balance = new_bal

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, new_bal):
        self._balance = new_bal

    @balance.getter
    def balance(self):
        return self._balance

    @balance.deleter
    def balance(self):
        print('Deleting balance..')
        del self._balance

if __name__ == '__main__':
    cust1 = Customer("Liza Binder", 2000)
    print(cust1.balance)
    cust1.balance = 3000
    print(cust1.balance)
    del cust1.balance
    print(cust1.name)
