import threading
import time

def walk_dog(first_name, last_name):
    time.sleep(8)
    print(f"{first_name} Walking the dog... {last_name}")

def cook_food():
    time.sleep(5)
    print("Cooking food...")

def clean_house():
    time.sleep(10)
    print("Cleaning the house...")


# walk_dog()
# cook_food()
# clean_house()

chore1 = threading.Thread(target=walk_dog,  args=("john", "doe"))
chore1.start()

chore2  = threading.Thread(target = cook_food)
chore2.start()

chore3 = threading.Thread(target = clean_house)
chore3.start()

chore1.join()
chore2.join()
chore3.join()
print("all chorete are  finished")
