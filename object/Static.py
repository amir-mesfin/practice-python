class employee:
    def __init__(self, name, position):
      self.name = name
      self.position = position
      
  
    def get_info(self):
      return f"{self.name} = {self.position}"  
    
    
    @staticmethod
    def  is_valid_position(position):
        valid_position = ["manager", "cashier", "cook", "janitor"]
        return position in valid_position
      
  
    
# print(employee.is_valid_position("cook"))
   
employee1 = employee("abushe", "manager")
employee2 = employee("ahmed", "cashier")
employee3 = employee("abdellah", "janitor")

print(employee.is_valid_position("rocket_scientist"))
print(employee1.get_info())
print(employee2.get_info())
print(employee3.get_info())


