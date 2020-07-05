"""
Create a function, is_palindrome, to determine if a supplied word is
the same if the letters are reversed.
"""


def is_palindrome(string):
    if string == string[::-1]:
        print("The string is a palindrome")
    else:
        print("Not a palindrome")


value = input("Enter a string:")
is_palindrome(value)
