# Object-Oriented Programming (OOP)
# Basic: Create a class called Car with attributes brand and color. Instantiate an object of the Car class and print its attributes.
# Intermediate: Add a method called start_engine to the Car class that prints a message saying the engine of the car has started. Create an instance of Car and call the method.
# Advanced: Create a class called BankAccount with attributes account_number and balance. Add methods to:
# Deposit an amount.
# Withdraw an amount (only if sufficient balance exists).
# Print the account balance.

#solution 1
class Car: # creating a class.
    def __init__(self,brand,color):# initializing the attributes.
        self.brand = brand
        self.color = color
my_car = Car("Toyota","black")
print(f"Brand : {my_car.brand}") #printing out the attributes of the car.
print(f"Color : {my_car.color}")

#solution2
class Car:
    def __init__(self,model,year):
        self.model = model
        self.year = year

    def  start_engine(self):
        print(f"The engine of the car {self.model},{self.year} has started.")
new_Car = Car("Harrier",2024)
new_Car.start_engine() # we call the function.


#solution3
class BankAccount:
    def __init__(self, account_number,balance = 0):
        self.account_number = account_number
        self.balance = balance
    def deposit(self,amount):
        if amount > 0:
            self.balance+= amount
            print(f"You have deposited {amount} and your account balance is {self.balance}")
        else:
            print(f"No deposit.")

    def withdraw(self,amount):
        if amount > 0:
            if amount <= 0:
              self.balance -= amount
              print(f"withdraw {amount}  and {self.balance}")
            else:
             print(f"Insufficient balance.")
        else:
            print(f"Withdraw amount must be positive.")
    def final_balance(self):
        print(f"Your balance is : {self.balance}")      


# Challenge: Implement a class called Library that manages a collection of books. Each book has a title, author, 
# and available status. The Library class should have methods to:
# Add a book to the library.
# Remove a book from the library.
# Check if a book is available by title.
# Borrow a book (mark it as unavailable if it’s available).
# Return a book (mark it as available again if it was borrowed).

#solution
class Library:
    def  __init__(self,title,author,available_status):
        self.title = title
        self.author = author
        self.available_status = available_status
        super(). __init__(title,author,available_status)
        
    