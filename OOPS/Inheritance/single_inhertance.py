# one child class and only one parent class

class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

        print("Dog barks")


dog = Dog()
dog.speak()  # Output: Animal speaks
dog.speak()   # Output: Dog barks