

try:
    number = input("Enter a number: ")
    result = 10 / int(number)
    print(f"Result is {result}")
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")