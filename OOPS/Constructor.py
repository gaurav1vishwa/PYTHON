class Student:
    def __init__(self , name , rollNumber, age, state):
        self.name = name
        self.rollNumber = rollNumber
        self.age = age
        self.state = state

    def information(self):
        print(f"Student Name is {self.name}")
        print(f"Student RollNumber is {self.rollNumber}")
        print(f"Student Age is {self.age}")
        print(f"Student State is {self.state}")


    def assignment(self):
        print(f"{self.name} has completed there assignment whose rollNumber is {self.rollNumber}");


stu = Student("Gaurav", 1, 22,"Madhya Pradesh");
stu.information();
stu.assignment();





class BankAccount:

    # Parameterized Constructor
    def __init__(self, accountHolder, accountNumber, balance):
        self.accountHolder = accountHolder
        self.accountNumber = accountNumber
        self.balance = balance

    # Method with parameter
    def deposit(self, amount):
        self.balance += amount
        print(f"₹{amount} deposited successfully.")

    # Method with parameter
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully.")
        else:
            print("Insufficient Balance!")

    # Method without parameter
    def display(self):
        print("\n----- Account Details -----")
        print(f"Account Holder : {self.accountHolder}")
        print(f"Account Number : {self.accountNumber}")
        print(f"Balance        : ₹{self.balance}")


# Object Creation
acc = BankAccount("Gaurav", 123456789, 10000)

# Display Original Details
acc.display()

# Deposit Money
acc.deposit(2500)

# Withdraw Money
acc.withdraw(4000)

# Display Updated Details
acc.display()
    
    