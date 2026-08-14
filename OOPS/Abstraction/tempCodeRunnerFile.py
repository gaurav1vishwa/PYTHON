from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass;


    @abstractmethod
    def stop(self):
        pass;

class AutoCar(Vehicle, ABC):
    pass;

class SelfAutoCar(Vehicle,ABC):
    def start(self):
        print("SelfAutoCar start");

    def stop(self):
        print("SelfAutoCar stop");

s = SelfAutoCar();
s.start();
s.stop();

