# 🐾 Base class
class Animal:
    def eat(self):
        print("Animal is eating.")

# 🐕 Middle class
class Dog(Animal):
    def bark(self):
        print("Dog is barking.")

# 🐶 Child class
class Puppy(Dog):
    def play(self):
        print("Puppy is playing.")

# 🧪 Test it
puppy1 = Puppy()
puppy1.eat()   # from Animal
puppy1.bark()  # from Dog
puppy1.play()  # from Puppy
