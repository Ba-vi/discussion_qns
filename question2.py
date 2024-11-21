# Lists
# Basic: Create a list of 5 fruits and print each fruit on a new line using a for loop.


#solution
fruits=["mangoes","oranges","berries","grapes","melon"]
for items in range(len(fruits)):
    print(fruits[items])

# Intermediate: Write a function that takes a list of numbers and returns a new list with each number squared. Example: [1, 2, 3] should become [1, 4, 9].

#solution


def square_numbers(numbers):
    square = []
    for num in numbers:
        square.append(num ** 2)
    return square

numbers = [1,2,3,4,5]
square = square_numbers(numbers)
print("The squares of the numbers are:", square)



# Advanced: Write a Python program that takes two lists, list1 = [1, 2, 3] and list2 = [4, 5, 6], and combines them into a single list, combined = [1, 4, 2, 5, 3, 6].

#solution
list_1 = [1,2,3]
list_2 = [4,5,6]
combined = []
for number in list_1:
     combined.append(number)
for num in list_2:
    combined.append(number)
print(combined)


# Challenge: Given a list of numbers, [3, 1, 4, 1, 5, 9, 2], write a program to find and print the two largest numbers in the list without using the max() function.

#solution4

def get_largest_two(numbers):
    
    number_sorted = sorted(numbers, reverse=True)# Sort the list in descending order
    
    
    return number_sorted[0], number_sorted[1]# Return the first two elements


numbers = [3, 1 ,4 , 1, 5, 9, 2]# Test the function with the given list
largest_two = get_largest_two(numbers)
print("The two largest numbers are:", largest_two)
