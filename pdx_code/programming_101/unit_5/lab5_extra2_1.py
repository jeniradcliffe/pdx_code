import string
import random

password = []
password_letters = string.ascii_letters 
password_digits = string.digits 
password_characters = string.punctuation

password_rdm_letters = []
password_rdm_digits = []
password_rdm_characters = []

password_length_letters = input("How many letters would you like your password to contain? ")
password_length_letters = int(password_length_letters)

password_length_digits = input("How many digits would you like your password to contain? ")
password_length_digits = int(password_length_digits)

password_length_characters = input("How many special characters would you like your password to contain? ")
password_length_characters = int(password_length_characters)

while len(password_rdm_letters) < password_length_letters:
    password_rdm_letters.append(random.choice(password_letters))

while len(password_rdm_digits) < password_length_digits:
    password_rdm_digits.append(random.choice(password_digits))

while len(password_rdm_characters) < password_length_characters:
    password_rdm_characters.append(random.choice(password_characters))

password = password_rdm_letters + password_rdm_digits + password_rdm_characters

random.shuffle(password)
print('Your password is: ' + ''.join(password))