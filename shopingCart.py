item = input("what item Would you like to  buy? : ")
price = float(input("what is the price? :"))
quality = int(input("how many would you like?"))

totalPrice = price * quality  
print(f"you hve bought {quality} X {item} \n total price is {totalPrice}$")   