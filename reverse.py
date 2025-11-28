weight = float(input("Enter Your weight"))
unit = input("Kilogram or Pounds")

if unit =="k":
  weight = weight * 2.205
  unit = "lbs "
  print(f"Your weight is : {round(weight, 1)} {unit}")
  
  
  