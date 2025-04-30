import json

class Vehicle:
    def __init__(self, name, color, year):
        self.__name = name  
        self.color = color
        self.year = year

    def repaint(self, new_color):
        self.color = new_color
 
    def display_info(self):
        print(f"Name: {self.__name}, Color: {self.color}, Year: {self.year}")

    # DATA PERSISTENCE

    def save_data(self, path):
        data = {
            "name": self.__name,
            "color": self.color,
            "year": self.year,
        }

        json_object = json.dumps(data)

        with open(path, "w") as file:
            file.write(json_object)

    def load_data(self, path):
        with open(path, "r") as file:
            json_object = json.load(file)
        
        self.__name = json_object["name"]
        self.color = json_object["color"]
        self.year = json_object["year"]

class Car(Vehicle):
    def __init__(self, name, color, year, brand):
        super().__init__(name, color, year)
        self.brand = brand
    def display_info(self):
        super().display_info()
        print(f"Brand: {self.brand}")

class Bicycle(Vehicle):
    def __init__(self, name, color, year, type):
        super().__init__(name, color, year)
        self.type = type

class Truck(Vehicle):
    def __init__(self, name, color, year, capacity):
        super().__init__(name, color, year)
        self.capacity = capacity
    def display_info(self):
        super().display_info()
        print(f"Capacity: {self.capacity}")

class Bus(Vehicle):
    def __init__(self, name, color, year, capacity):
        super().__init__(name, color, year)
        self.capacity = capacity
    def display_info(self):
        super().display_info()
        print(f"Capacity: {self.capacity}")
    def repaint(self, new_color):
        if not new_color == "Yellow":
            print()
            print("You can't repaint a school bus, they're canonically yellow!")
        else:
            self.color = new_color

def display_vehicle_info(vehicle):
    vehicle.display_info()

vehicles = [
    Car("SUV", "Black", 2023, "Toyota"),
    Bicycle("Sport", "Red", 1990, "Mountain"),
    Truck("Pickup", "White", 2011, "5000 lbs"),
    Bus("School", "Yellow", 2021, 38)
]

vehicles[0].repaint("Blue")
vehicles[3].repaint("Purple")

print()
print("Vehicle Info")
for vehicle in vehicles:
    print()
    vehicle.display_info()

print()

#vehicle = Vehicle("Titanic", "White, Black", 1912)
#vehicle.save_data("data.json")

vehicle = Vehicle("HMS Beagle", "Black, Yellow", 1820)
vehicle.display_info()
vehicle.load_data("data.json")
vehicle.display_info()
