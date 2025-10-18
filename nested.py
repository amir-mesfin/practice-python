
row  = int(input("enter the the number row :  "))
column = int(input("Enter the number column :  "))
symbol = (input("Enter the symbol to use :  "))

for x in range(row):
   for c in range(column):
     print(symbol, end="")
   print() 