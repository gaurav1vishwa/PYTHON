#Method Overriding (run - time ploymorphism)


class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        super().speak()  # Calling the parent class method
        print("Dog barks")

class Cat(Animal):
    def speak(self):
        super().speak()  # Calling the parent class method
        print("Cat meows")

# Creating objects of each class
cat = Cat()
cat.speak();
dog = Dog()
dog.speak();