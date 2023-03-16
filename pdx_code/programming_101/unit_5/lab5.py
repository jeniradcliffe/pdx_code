import string
import random

password = []
password_characters = string.ascii_letters + string.digits + string.punctuation

while len(password) < 10:
    password.append(random.choice(password_characters))

print(''.join(password))
