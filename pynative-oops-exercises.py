class Vehicle:
    # Class attribute.
    color = "White"

    def __init__(self, name, max_speed, mileage, capacity = 40):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        self.capacity = capacity

    def get_name(self):
        return self.name

    def seating_capacity(self, capacity):
        return f"The seating capacity of {self.name} is {capacity} passengers."

    def fare(self):
        return self.capacity * 100

class Bus(Vehicle):
    def __init__(self, name, max_speed, mileage, wheels, capacity = 40):
        super().__init__(name, max_speed, mileage, capacity)
        self.wheels = wheels
    
    def get_wheels(self):
        if self.wheels == 2:
            print("Two Wheeler")
        elif self.wheels == 3:
            print("Three Wheeler")
        elif self.wheels == 4:
            print("Four Wheeler")
        else:
            print("Unknown Wheeler")

    def seating_capacity(self, capacity = 50):
        return f"The seating capacity of {self.get_name()} is {capacity} passengers."

    def fare(self):
        return super().fare() * 1.1

class Car(Vehicle):
    pass

def inheritance_1():
    bus = Bus("Leyland", "90", "40 kmpl", 5)
    bus.get_name()
    bus.get_wheels()

def inheritance_2():
    ob = Car()
    print('Empty class\'s object created.')

def inheritane_4():
    ob = Bus("Leyland", "120", "40 kmpl", 4)
    print(ob.seating_capacity())

def inheritance_5():
    bus = Bus('Volvo', "100", "40 kmpl", 4)
    audi = Car('Audi', "220", "80 kmpl")
    print(bus.get_name() + ": " + bus.color)
    print(audi.get_name() + ": " + audi.color)

def inheritance_6():
    bus = Bus('Volvo', "100", "40 kmpl", 4, 50)
    print(bus.fare())

def inheritance_7():
    bus = Bus('Volvo', "100", "40 kmpl", 4, 50)
    print(type(bus))

def inheritance_8():
    bus = Bus('Volvo', "100", "40 kmpl", 4, 50)
    print(isinstance(bus, Vehicle))

# Problems map is a dictionary mapping the serial number with its solver function.

problems = {
    '1': inheritance_1,
    '2': inheritance_2,
    '4': inheritane_4,
    '5': inheritance_5,
    '6': inheritance_6,
    '7': inheritance_7,
    '8': inheritance_8,
}

# main() is the root function from where the other functions are called
# depending on problem number provided in selection

def main():
    global problems
    option = input('Selection: ')

    problems[option]()

main() # Run the root function.