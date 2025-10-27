# 🐾 Base Class
class Animal:1
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")


# 🏡 Base Class 2
class Pet:
    def __init__(self, owner):
        self.owner = owner

    def show_owner(self):
        print(f"This pet belongs to {self.owner}.")

    def play(self):
        print(f"{self.owner}'s pet is playing happily! 🐾")


# 🐶 Child Class (inherits from both Animal and Pet)
class PetDog(Animal, Pet):
    def __init__(self, name, owner, breed):
        # Call both parent constructors
        Animal.__init__(self, name)
        Pet.__init__(self, owner)
        self.breed = breed

    def speak(self):
        print(f"{self.name} says: Woof! 🐕")

    def info(self):
        print(f"{self.name} is a {self.breed} owned by {self.owner}.")


# 🧠 Create Object
dog1 = PetDog("Buddy", "Amir Mesfin", "Golden Retriever")

# 🐾 Using methods from both parent classes
print("--- Multiple Inheritance Demo ---")
dog1.eat()         # from Animal
dog1.sleep()       # from Animal
dog1.show_owner()  # from Pet
dog1.play()        # from Pet
dog1.speak()       # from PetDog
dog1.info()        # from PetDog
