import string
import random

password = []
password_letters = string.ascii_letters 
password_digits = string.digits 
password_characters = string.punctuation

password_rdm_letters = []
password_rdm_digits = []
password_rdm_characters = []

length = input("How many letters, digits, and characters would you like your password to contain? ")
length_list = length.split(",")
# print(f"{length_list}")
length_ints = [int(item) for item in length_list]
sum_length = sum(length_ints)
num_letters = length_ints[0]
num_digits = length_ints[1]
num_characters = length_ints[2]

while len(password) < sum_length:

    while len(password_rdm_letters) < num_letters:
        password_rdm_letters.append(random.choice(password_letters))
    while len(password_rdm_digits) < num_digits:
        password_rdm_digits.append(random.choice(password_digits))
    while len(password_rdm_characters) < num_characters:
        password_rdm_characters.append(random.choice(password_characters))
    password = password_rdm_letters + password_rdm_digits + password_rdm_characters

random.shuffle(password)
print('Your password is: ' + ''.join(password))
