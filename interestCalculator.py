principle = 0
rate = 0
time = 0


while principle <= 0:
    principle = float(input("enter the principle amount : "))
    if principle <= 0:
        print("principle con't be less than or equal to zero ")

while rate <= 0:
    rate = float(input("enter the rate amount : "))
    if rate <= 0:
        print("rate con't be less than or equal to zero ")
    else:
        break
while time <= 0:
    time = int(input("enter the time amount : "))
    if time <= 0:
        print("time con't be less than or equal to zero ")
    else :
        break

print(f"principle is : $ {principle}")
print(f"rate is :  {rate}")
print(f"time is: {time} years")


total = principle * pow((1+rate/100), time)


print(F"balance after {time} years/s:  ${total:.2f}")
