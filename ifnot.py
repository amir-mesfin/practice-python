high_income = input("high income (yes/no): ").lower() == "yes"
good_income = input("good income (yes/no): ").lower() == "yes"
student = input("student (yes/no): ").lower() == "yes"

if high_income or good_income and not student:
    print("Eligible for loan")
else:
    print("Not eligible")
 