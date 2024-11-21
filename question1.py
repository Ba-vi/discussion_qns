
# Loops
# Basic: Write a Python program that prints all even numbers between 1 and 20 using a for loop.

#solution
def even_numbers():
    for even in range(1,21):
        if even % 2 == 0:
         print(even)
even_numbers()        




# Intermediate: Use a while loop to ask the user to input a number until they provide a number greater than 10.

number= int(input("Please enter a number:"))
while number <= 10:
    print(f"The number is not greater than 10.")
    number=int(input("Please enter a number greater than 10:"))
print(f"Thank you! The number {number} you've entered is greater than 10.")


# Advanced: Write a program that prints the multiplication table (from 1 to 10) for numbers from 1 to 5 using nested for loops.

for m in range(1,6):   #loop for numbers 1-5
    print(f"Multiplication table for {m}:")
    
    for n in range(1,11):   #loop through numbers 1-10
      print(f"{m} x {n} = {m*n}")
print() # printing a new line for seperation between tables.


# Challenge: Given a list of integers, [4, 7, 2, 9, 12, 15], write a program using a for loop to find the sum of all odd numbers and print the result.
numbers = [4,7,2,9,12,15] #list of the integers

odd_sum = 0#initializing the variable to store the sum of odd numbers.
for num in numbers:
        if num  % 2 != 0: # check if the number is odd
            odd_sum += num #add the number to the sum
print(f"The sum of all odd numbers is :",odd_sum)



