# Duck Typing means that the type or class of an object is less important than the methods it defines.

class Dog:
    def swim(self):
        print("Dog is swimming")

class Duck:
    def swim(self):
        print("Duck is swimming")


#Funcetion is using the duck typing
def make_swim(obj):
    obj.swim()

d = Dog()
dc = Duck()
make_swim(d)  # Output: Dog is swimming
make_swim(dc)  # Output: Duck is swimming



class Parrot:
    def fly(self):
        print("Parrot is flying")

class Airplane:
    def fly(self):
        print("Airplane is flying")


def make_fly(obj):
    obj.fly()

p = Parrot()
a = Airplane()
make_fly(p)  # Output: Parrot is flying
make_fly(a)  # Output: Airplane is flying