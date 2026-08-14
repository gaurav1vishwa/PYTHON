# Abstraction is the process of hiding implementation details an showing only the essential features to the user 

# using: ABC (abstract class), abstract method, 


# repeatation code right
class Vehicle:
    def start(self):
        print("Every vehicle start manually");

    def stop(self):
        print("Every vehicle stop manually");


class Car():
    def start(self):
        print("Every can start automatically");

    def stop(self):
        print("Every car stop automatically");

v = Vehicle();
v.start()
v.stop();

c = Car();
c.start()
c.stop()

# if we inherit  than also nothing error but it is repeatation right
# what ever the method defeid here there are concrete method means here only you have to implements these
class Vehicle:
    def start(self):
        print("Every vehicle start manually");

    def stop(self):
        print("Every vehicle stop manually");


class Car(Vehicle):
    def start(self):
        print("Every can start automatically");

    def stop(self):
        print("Every car stop automatically");

v = Vehicle();
v.start()
v.stop();

c = Car();
c.start()
c.stop()

# so basically the concept of absraction is to only show the necessary thing and anything that's not need to show the user 
# you just hide from the user by the use of absract class and absract mehtod both 
# this problem can be solver by the abstraction let's see
# if you want to abstract method you should defiend the abstract method (at least one ) 
# abstract class can have combination of abstract method  as well as concrete method
# for archiving the abstraction you need to import the asbstraction from the built-in library called abc 
# absract mehtod means - such mehtod that not the method body;
# we can not careate the object of the absract class so if need to use it we can override the absract method in the 
# child class and than we can can use it by creating the object of it 
# 100% abstraction only can be archived when all the method in the abstract class should be abstract method 


from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass;
# this is concrete mehod
    def stop(self):
        print("Every vehicle stop manually");


class Car(Vehicle):
    def start(self):
        print("Every can start automatically");

    def stop(self):
        print("Every car stop automatically");

c = Car();
c.start()
c.stop()