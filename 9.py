"""
Write a binary search function. It should take a sorted sequence and the item it is looking for.
It should return the index of the item if found. It should return -1 if the item is not found.
"""


def binary_search(lis, search_value):
    try:
        index = lis.index(search_value)
    except ValueError:
        index = -1

    return index


lis_value = []
inp = int(input("Enter the number of  items in the list:"))
for i in range(inp):
    value = input("Enter list item:")
    lis_value.append(value)
lis_value.sort()
search = input("ENter the value you want to search:")
result = binary_search(lis_value, search)
print(f'The index is {result}')
