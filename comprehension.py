double = []

for x in range(11):
  
  double.append(x*x)
  
print(double)

name = ["abushe", "amir", "belachew", "mohamed", "amirachn"]

name_upper = [item.upper() for item in name]
name_first_char = [name1[0].upper() for name1 in name]
name3 = [name1.upper() for name1 in name if name1[0]== "a"]


print(name_upper)
print(name_first_char)
print(name3)

