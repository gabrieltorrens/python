class Vehicle():
    def __init__(self, bodystyle): #init function
        self.bodystyle = bodystyle #holds the value that was passed in
    
    def drive(self,speed):
        self.mode = "driving"
        self.speed = speed

class Car(Vehicle):
    def __init__(self, enginetype):
        super().__init__("Car")
        self.wheels = 4
        self.doors = 4
        self.engine = enginetype
    def drive(self, speed):
        super().drive(speed)
        print("Driving my", self.engine, "car at", self.speed)

class Motorcycle(Vehicle):
    def __init__(self, enginetype, hassidecar):
        super().__init__("Motorcycle")
        if (hassidecar):
            self.wheels = 3
        else:
            self.wheels = 2
        self.doors = 0
        self.engine = enginetype
    
    def drive(self, speed):
        super().drive(speed)
        print("Driving my", self.engine, "motorcycle at", self.speed)

car1 = Car("gas")
car2 = Car("hybrid")
motorcycle1 = Motorcycle("gas", True)

print(car1.wheels)
print(motorcycle1.engine)

car1.drive(30)
motorcycle1.drive(50)