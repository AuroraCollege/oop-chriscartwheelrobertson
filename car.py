
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

        self.mileage = 0.0
        self.fuel_used = 0.0

    def add_mileage(miles):
        self.mileage += miles

    def add_fuel_usage(gallons):
        self.fuel_used += gallons

    def calculate_fuel_efficiency():
        return self.mileage / self.fuel_used

car1 = Car('Toyota', 'Camry', 1994)
car2 = Car('Mitsubishi', 'Pajero', 2002)
car3 = Car('DeLorean', "DMC-12", 1981)

print(car1.make)
print(car2.model)
print(car3.year)