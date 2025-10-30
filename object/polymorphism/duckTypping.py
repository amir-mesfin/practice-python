#  duck typing

class animal:
    alive = True


class dog(animal):
    def speak(self):
        print("woof")


class cat(animal):
    def speak(self):
        print("meow")


class car:
    alive = True

    def speak(self):
        print("HONK")


animals = [cat(), dog(), car()]

for animal in animals:
    animal.speak()
    print(animal.alive)
