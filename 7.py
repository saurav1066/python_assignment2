"""
Create a list of tuples of first name, last name, and age for your friends and colleagues. If you don't know the age,
put in None. Calculate the average age, skipping over any None values.
 Print out each name, followed by old or young if they are above or below the average age.
"""

name_tuple = ('Saurav', 'Adhikari', 23)
count = 0
average_age = 0
people = [name_tuple]
inp = int(input("how many friends you wanna add:"))
for i in range(inp):
    first_name = input("Enter first name:")
    last_name = input("Enter last name:")
    age = input("Enter the age:")
    try:
        age = int(age)
    except ValueError:
        age = None
    people.append((first_name, last_name, age))

for i in people:
    if i[2] is not None:
        average_age += i[2]
        count += 1
average_age = average_age / count

for i in people:
    if i[2] is not None:
        if i[2] > average_age:
            print(f'{i[0]} {i[1]}, old')
        else:
            print(f'{i[0]} {i[1]}, young')
