# Hierarchical Inheritance one parent class is inherited by multiple child classes

class Parent:
    def skills(self):
        return "Gardening, Programming"

class Child1(Parent):
    pass

class Child2(Parent):
    pass


print(Child1().skills(), Child2().skills()) # Gardening, Programming