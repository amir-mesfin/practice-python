menu = {
    "pizza": 34.00,
    "nachos": 35.00,
    "popcorn": 45.00,
    "soda": 67.00,
    "lemonade": 4.78,
    "chips": 32.78
}
cart = []
total = 0
print("********************************")
print("------------  menu  ------------")
print()

for key, values in menu.items():
    print(f"{key:10}......${values:.2f}")

print()
print("********************************")


while True:
    food = input("select an item (q to quite) :  ")
    if food.lower() == 'q':
        break
    elif menu.get(food) is not None:
        cart.append(food)

for food in cart:
    total += menu.get(food)
    
print()
print("-----------------  YOUR ORDER  ---------------")

for food in cart:
  print(food, end = " ")

print(f"\n   Total is : ${total}")
 