def sum(numbers):
    numbers_length = len(numbers)
    sum_numbers = 0
    for i in range(numbers_length):
        sum_numbers = sum_numbers + numbers[i]
    return sum_numbers

numbers = []

while True:
    number = input("Enter a number or 'done' to quit: ")

    if number != "done":
        number = int(number)
        numbers.append(number)

    else:
        break
    
print(f"You entered {numbers} \n The sum of the numbers is {(sum(numbers))}")    
