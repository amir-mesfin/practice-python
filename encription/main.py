import random
import string


chars = " " + string.punctuation + string.digits + string.ascii_letters

char_list = list(chars)

key = char_list.copy()
random.shuffle(key)
print(f"char____{char_list}")
print(f" key______{key}")

# incription

plain_text = input("enter your message to encript: ")#
cipher_text = ""

for letter in plain_text:
    index = char_list.index(letter)
    cipher_text += key[index]


print(f"cipher text : {cipher_text}")
print(f"orginal text : {plain_text}")


# decription_text = ""
encription = input("enter your message to decript: ")

decription_text = ""

for letter in encription:
    index = key.index(letter)
    decription_text += char_list[index]


print(f"cipher text : {cipher_text}")
print(f"orginal text : {decription_text}")
