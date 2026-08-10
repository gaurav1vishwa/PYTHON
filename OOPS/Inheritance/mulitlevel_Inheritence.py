# Multilevel Inheritance its like chanining of classes 

class GreatGrandParent:
    def __init__(self):
        print("Great Grand Parent Constructor");

class GrandParent(GreatGrandParent):
    def __init__(self):
        print("Grand Parent Constructor");
        super().__init__();

class Parent(GrandParent):
    def __init__(self):
        print("Parent Constructor");
        super().__init__();

class Child(Parent):
    def __init__(self):
        print("Child Constructor");
        super().__init__();

c = Child();