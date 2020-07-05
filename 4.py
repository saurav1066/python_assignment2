"""
Create a list. Append the names of your colleagues and friends to it. Has the id of the list changed? Sort the list.
What is the first item on the list? What is the second item on the list?
"""

name_list = ["Saurav", "Hitesh", "Ram", "Shyam"]
init_id = id(name_list)
inp = input("Enter the name of your colleagues:")
name_list.append(inp)
final_id = id(name_list)
if init_id == final_id:
    print("The id is the same")
else:
    print("The id changed")
name_list.sort()
print(f'The first item in list {name_list[0]}')
print(f'The second name in list {name_list[1]}')