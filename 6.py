"""
Create a list with the names of friends and colleagues. Search for the
name ‘John’ using a for a loop. Print ‘not found’ if you didn't find it.
"""

name_list = []
inp = int(input("How many names u want to put in list:"))
for i in range(inp):
    value = input("Enter a name:")
    name_list.append(value)

for i in name_list:
    if i == "john":
        print("john found")
        break

else:
    print("Not Found")
