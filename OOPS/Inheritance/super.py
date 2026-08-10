# super keyword - used to refears to the parent class methods and variables, 
# it is used to avoid the ambiguity when the parent class and child class have same method name or variable name.
#and also use for calling the parent class constructor from the child class constructor.

class A:
    def show(self):
        print("This is a");

class B(A):
    def show(self):
        print("This is b");
        super().show(); # calling the parent class method

b = B();
b.show();



# using by constructor 
print("-------------------- Constructor --------------------")


class A:
    def __init__(self, name):
        self.name = name
        print("This is a constructor of class A")
        print("Name is:", name)


class B(A):
    def __init__(self, name):
        super().__init__(name)
        print("This is a parameterised constructor of class B")
        print("Name is:", name)


class C(A):
    def __init__(self):
        print("This is a constructor of class C")
        super().__init__("Gaurav")

c = C()


print("-------------------- Constructor --------------------")


class A:

    # Default constructor
    def __init__(self, name="Default"):
        self.name = name
        print("Constructor of A")
        print("Name:", self.name)


class B(A):

    # Parameterized constructor
    def __init__(self, name):
        super().__init__(name)
        print("Parameterized constructor of B")
        print("Name:", self.name)


class C(A):

    # Default constructor
    def __init__(self):
        print("Default constructor of C")

        # Calling A's constructor with parameter
        super().__init__("Gaurav")


# C object
c = C()

# B object
b = B("Rahul")

# A object without parameter
a1 = A()

# A object with parameter
a2 = A("Amit")



