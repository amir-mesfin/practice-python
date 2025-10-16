userName = input("enter user name:  ")

if len(userName) >12 :
   print("please inter less than the 12")
elif userName.find(" ") != -1 :
   print("please do not enter the space")
elif not userName.isalpha() :
  print("please do not enter the number")
else :
  print(f" welcome {userName} ")