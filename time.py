import time

my_time = int(input("Enter the time in the second"))
# time.sleep(3)

for x in range(my_time, 0, -1) :
  second= x % 60
  minutes = int(x/60) % 60
  hour = int(x/3600) 
  
  print(f"{hour:02}:{minutes:02}:{second:02}")
  time.sleep(1)
   

print("time up")