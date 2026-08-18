class Bank:

    def __init__(self):
        self.__balance = 25000 # private variable

    # getter
    def get_balance(self):
        print(f"The balance is {self.__balance}")

    # setter
    def set_balance(self, new_balance):
        if new_balance < 0:
            print("No balance")
        else:
            self.__balance = new_balance


b = Bank()

b.get_balance()

b.set_balance(1000000)

b.get_balance()

#Name Mangling (object reference._classname__attr); it is used to access the private field without getter and setter
print(b._Bank__balance);


 