'''Use % to get the remainder of the grade when divided by ten, which is the same as the number in the ones digit. The number in the ones digit will determine whether they will get a '+' or a '-' appended to the end of their grade.

For example, the grade 81 would be a 'B'. 81 % 10 would give you 1, which is a low number, so you would add a '-' to the end of the grade.'''

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

plusminus = number % 10
# print(grade,plusminus)

if number != 100 and grade != "F" and plusminus >= 5:
    plusminus = "+"

elif number != 100 and grade != "F":
   plusminus = "-"

if plusminus == "+" or plusminus == "-":
    print(grade,plusminus)

else:
    print(grade)