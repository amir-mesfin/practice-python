import time 

def count(start, end):
  for x in range(start, end):
    print(x)
    time.sleep(1)
  print("done")
  
count(0,10)
  
def function(**kwargs):
  print(kwargs)
  for key, value in kwargs.items():
    print(f"{key} : {value}")
     
  
print(function(name4= "name", name3="abushe" , name2="hello", name1="Amir"))


student = {"name": "Abushe", "age": 22, "country": "Ethiopia"}

print("name" in student)          # True
print("Abushe" in student)        # False (value, not key)
print("country" not in student)   # False


