# 🐾 Base Class
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")


# 🐕 Level 2: Dog class inherits from Animal
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)   # Call parent (Animal) constructor
        self.breed = breed

    def bark(self):
        print(f"{self.name} says: Woof! 🐕")

    def info(self):
        print(f"{self.name} is a {self.breed} dog.")


# 👮 Level 3: PoliceDog inherits from Dog
class PoliceDog(Dog):
    def __init__(self, name, breed, unit):
        super().__init__(name, breed)   # Call Dog’s constructor
        self.unit = unit

    def duty(self):
        print(f"{self.name} is on duty with the {self.unit} unit 🚓.")

    def info(self):
        # Override info() to add more details
        print(f"{self.name} is a {self.breed} working in the {self.unit} unit.")


# 🧠 Create Object
rex = PoliceDog("Rex", "German Shepherd", "K9")

# 🐾 Demonstrate multilevel inheritance
print("--- Multilevel Inheritance Demo ---")
rex.eat()        # From Animal
rex.sleep()      # From Animal
rex.bark()       # From Dog
rex.duty()       # From PoliceDog
rex.info()       # Overridden method from PoliceDog
