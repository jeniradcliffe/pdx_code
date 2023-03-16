def remove_all(numbers, target):
    # print(numbers, type(numbers))
    numbers = list(filter((target).__ne__, numbers))
    return numbers


# numbers = input("Please insert a list of numbers: ")
# numbers = numbers.split(",")
# numbers = list(numbers)
# target = input("Please specify the number to be removed from the list: ")

numbers = [4, 5, 4, 2, 7, 4, 4, 5, 8, 10]
target = 4

print(remove_all(numbers,target))    
