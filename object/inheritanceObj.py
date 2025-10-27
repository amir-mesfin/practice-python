# 🐾 Base (Parent) Class
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")


# 🐶 Child Classes (Inherit from Animal)
class Dog(Animal):
    def speak(self):
        print(f"{self.name} says: Woof! 🐕")


class Cat(Animal):
    def speak(self):
        print(f"{self.name} says: Meow! 🐱")


class Mouse(Animal):
    def speak(self):
        print(f"{self.name} says: Squeak! 🐭")


# 🧠 Creating objects (instances)
dog1 = Dog("Buddy")
cat1 = Cat("Whiskers")
mouse1 = Mouse("Mickey")

# 🐾 Using inherited methods
print("--- Animal Actions ---")
dog1.eat()
cat1.sleep()
mouse1.eat()

# 🗣️ Using subclass-specific methods
print("\n--- Animal Sounds ---")
dog1.speak()
cat1.speak()
mouse1.speak()
