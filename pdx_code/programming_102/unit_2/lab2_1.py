def sum(numbers):
    numbers_length = len(numbers)
    sum_numbers = 0
    for i in range(numbers_length):
        sum_numbers = sum_numbers + numbers[i]
    return sum_numbers

numbers = [4, 5, 4, 2, 7, 4, 4, 5, 8, 10]
print(sum(numbers))