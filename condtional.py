# name = input("please enter your name : ")

# if name == "" :
#   print("you must enter the name")
# else:
#   print(f"hello {name} i miss you dude")


num1 = float(input("please inter the number :  "))

operator = input(" Enter the operator (-, /, *,  %, and +)")

num2 = float(input("please inter the number :  "))


if operator == "-":
    result = round(num1 - num2)
    print(f"the result {num1} {operator} {num2} = {result}")
    
elif operator == "/":
    result = round(num1 / num2)
    print(f"the result  of {num1} {operator} {num2} = {result}")
    
elif operator == "+":
    result = num1 + num2
    print(f"the result {num1} {operator} {num2} = {result}")
    
elif operator == "%":
    result = num1 % num2
    print(f"the result {num1} {operator} {num2} = {result}")
    
elif operator == "*":
    result = num1 * num2
    print(f"the result {num1} {operator} {num2} = {result}")
    
else :
    print(f"{operator} is not  uu valid")  
    
  


