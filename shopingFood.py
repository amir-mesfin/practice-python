foods = []
prices = []
total = 0

while True:
    food = input("Enter  a food to buy (q to quit) : ")
    if food.lower() == "q":
        break
    else:
      price = float(input(f"Enter the price of a {food}: $"))
      foods.append(food)
      prices.append(price)
      
print("____________ YOUR CART _________________")

for food in foods:
  print(food, end=" ")
  
  
for price in prices:
  total +=price 
   
print(f"\ntotal price of  the food is : ${total}")
  
  
print("\n_________________________________________")

