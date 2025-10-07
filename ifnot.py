high_income = input("high income (yes/no): ").lower() == "yes"
good_income = input("good income (yes/no): ").lower() == "yes"
student = input("student (yes/no): ").lower() == "yes"


if high_income or good_income and not student:
    print("Eligible for loan")
else:
    print("Not eligible")
print("done")


for number in range(3):
  print(number)

for number in range(2, 12, 3):
  print(number)
  if number == 8:
     print("successful")
     break
  else:
     print("no Eligible")

for X in range(5):
   for y in range(4):
     print(f"{X}, {y}")

print(type(range(5)))

number = 100
while number > 0:
    print(number)
    number = number // 2


command = ""
while command != "quit" :
  command = input(">")
  print("ECHO", command)

while True :
  command = input(">")
  print(" ECHO", command)
  if command.lower() == "quit":
    break

for number in range(2,10,2):
  print(number)
print("we have 4 enven number")

count = 0
get = int(input("enter the the number " ))
for number in range(1,get):
  if number % 2 == 0:
   count += 1
   print(number)

print(f"we have {count} even")


def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


result = multiply(2, 4, 5, 6)
print(result)
