name = input("inter the string example:  ")
phone_number = (input("enter your phone number:  "))
# result = len(name)
result = name.find(" ")
resultF = name.rfind(" ")


print(result)
print(f" revese index {resultF}")

print(f"capitalization  {name.capitalize()}")
print(f"upper  {name.upper()}")
print(f"capitalization  {name.capitalize()}")
print(f"check only digit   {name.isdigit()}")
print(f"how mach they founded   {phone_number.count("-")}")
print(f"replace the    {phone_number.replace("-",' ', 2)}")
