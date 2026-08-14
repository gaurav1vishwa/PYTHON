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