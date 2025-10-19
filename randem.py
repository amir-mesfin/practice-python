import random

# print(help(random))

# number = random.randint(1,6)

# print(number)

card = [1,2,4,5,6,78]

print(random.choice(card))

print(random.choices(card, k=3))

print(random.shuffle(card))

print(random.random())