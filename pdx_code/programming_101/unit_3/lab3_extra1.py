'''Use the random module's randint() function to determine the user's rival's score.

Grade the rival's score as well
Compare the user's score to the rival's score
Let the user know if they did better than their rival.
Display the result along with both student's scores and letter grades.'''

number = input("Please enter a number between 0-100: ")
number = int(number)
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

# print(grade)

import random
number_rand = random.randint(1,100)

# print(number, number_rand)

if number_rand >= 90 and number_rand <= 100:
    grade_rand = "A"

elif number_rand >= 80 and number_rand <= 89:
    grade_rand = "B"

elif number_rand >= 70 and number_rand <= 79:
    grade_rand = "C"

elif number_rand >= 60 and number_rand <= 69:
    grade_rand = "D"

elif number_rand >= 0 and number_rand <= 59:
    grade_rand = "F"

if number_rand == number:
    message = "You scored the same as your rival."

elif number_rand < number:
    message = "You scored better than your rival."

elif number_rand > number:
    message = "You scored worse than your rival."

print(f"Your grade: {number} which is {grade}. Your rival's grade: {number_rand} which is {grade_rand}. {message}")