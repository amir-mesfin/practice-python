# high_income = input("high income (yes/no): ").lower() == "yes"
# good_income = input("good income (yes/no): ").lower() == "yes"
# student = input("student (yes/no): ").lower() == "yes"



# if high_income or good_income and not student:
#     print("Eligible for loan")
# else:
#     print("Not eligible")
# print("done")


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