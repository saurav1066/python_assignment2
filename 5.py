"""
Create a tuple with your first name, last name, and age. Create a list,
people, and append your tuple to it. Make more tuples with the corresponding information from your friends and
append them to the list. Sort the list. When you learn about sort method, you can use the key parameter to sort
by any field in the tuple, first name, last name, or age.
"""

name_tuple = ('Saurav', 'Adhikari', 23)
people = [name_tuple]
first_name = input("Enter first name:")
last_name = input("Enter last name:")
age = int(input("Enter the age:"))
people.append((first_name, last_name, age))
print(people)
print(sorted(people))
print(sorted(people, key = lambda x : x[2]))


