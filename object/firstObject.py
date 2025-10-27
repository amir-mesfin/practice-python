class Car:
    def __init__(self, model, year, color, for_rent):
        self.model = model
        self.year = year
        self.color = color
        self.for_rent = for_rent
    def drive(self):
      print(f"you drive the car  {self.color} {self.model}")
    def stop(self):print(f"You stop the car {self.color} {self.model}")
    
    def describe(self):
        print(f"{self.year} {self.color} {self.model}")
      
car1 = Car("Toyota", 2024, "Red", True)
car2 = Car("charger", 2025, "blue", False)
car3 = Car("mustang", 2020, "green", True)

# print(car1.model)
# print(car1.year)
# print(car1.color)
# print(car1.for_rent)

car1.drive()
car2.stop()

car1.describe()
car2.describe()
car3.describe()