# Dictionaries
# Basic: Create a dictionary with three key-value pairs representing a student's information: name, age, and grade. Print each key-value pair on a new line.
# Intermediate: Write a function that takes a dictionary of people's names and their ages,{ 'Alice': 24, 'Bob': 19, 'Charlie': 30}, and returns a list of names of people who are 21 or older.
# Advanced: Given a dictionary representing items in a store with their prices, {'apple': 0.5, 'banana': 0.3, 'orange': 0.7}, write a program that takes a list of items bought, ['apple', 'orange', 'banana', 'banana'], and calculates the total cost.
# Challenge: Write a program that counts the occurrences of each word in a given sentence. Example: for the sentence "hello world hello," the output should be {'hello': 2, 'world': 1}.

#solution1
dict={
     "name":"Violah",
     "age" :22,
     "grade" :" Grade A"
}
name = dict["name"]
print(name)

age = dict["age"]
print(age)

grade = dict["grade"]
print(grade)



#solution 2
student = { "name":'Alice',"age": 24,"name" :'Bob',"age": 19, "name":'Charlie',"age": 30}

for students in student:
    if  student["age"] >=20:
       print(f"The students are :{student["name"]},{student["age"]}")
    

#solution3

prices = {
    'apple': 0.5,
    'banana': 0.3,
    'orange': 0.7
}

# List of items bought
items_bought = ['apple', 'orange', 'banana', 'banana']

total_cost = 0
for item in items_bought:#looping through items bought.
    if item in prices:  # Check if the item is in the prices dictionary
        total_cost += prices[item]

print(f"The total cost of the items bought is: {total_cost}")


#solution4

def count_word_occurrences(sentence):
    sentence = "hello world hello".lower()
    words = sentence.split() # Split the sentence into words

    word_count = {} # Create a dictionary to store the word counts
    for word in words:
        if word in word_count:
            word_count[word] += 1  # Increment the count if the word is already in the dictionary
        else:
            word_count[word] = 1  # Add the word to the dictionary with a count of 1

    return 
result = count_word_occurrences("sentence")

sentence = "hello world hello"
print(result)# Call the function and print the result




