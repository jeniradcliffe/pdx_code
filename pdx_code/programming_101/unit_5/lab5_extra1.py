import string
import random

password = []
password_characters = string.ascii_letters + string.digits + string.punctuation

length = input("How many characters would you like your password to contain? ")
length = int(length)

while len(password) < length:
    password.append(random.choice(password_characters))

print(''.join(password))
