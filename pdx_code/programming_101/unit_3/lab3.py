number = input("Please enter a number between 0-100: ")
number = float(number)
# print(type(number))

if number >= 90 and number <= 100:
    grade = "A"

elif number >= 80 and number <= 89:
    grade = "B"

elif number >= 70 and number <= 79:
    grade = "C"

elif number >= 60 and number <= 69:
    grade = "D"

elif number >= 0 and number <= 59:
    grade = "F"

else:
    grade = "Your number is not between 0-100"

print(grade)