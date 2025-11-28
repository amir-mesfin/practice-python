# weight = float(input("Enter Your weight"))
# unit = input("Kilogram or Pounds")

# if unit =="k":
#   weight = weight * 2.205
#   unit = "lbs "
#   print(f"Your weight is : {round(weight, 1)} {unit}")
  
# num = float(input("Enter number :")) 
  
# result = "posetive" if num >0 or num == 0  else "Negative"

# print(result)

# import math

# print(math.max(34, 56,567))

# creadit_card = "134-56745-7843"

# print(credit_card[::-1])

# print(creadit_card.find("3"))
# print(creadit_card.rfind("3"))
# print(len(creadit_card))
# print(creadit_card.isalpha())
# print(creadit_card.isdigit())
# print(creadit_card.count("3"))
# print(creadit_card.replace("3","4" ))


foods = []
prices = []
totalPrice = 0 

while True:
  food = input("Enter a Food  to buy (q to quit)")
  if food.lower() == "q":
    break
  else :
    price = float(input(f"Enter the price of a {food}: $")) 
    foods.append(food)
    prices.append(price)

print