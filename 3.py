"""
Write code that will print out the anagrams (words that use the same letters) from a paragraph of text.
"""

anagram = input("Enter the substring you want to search:")
paragraph = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
word_list = paragraph.split()
for i in word_list:
    if anagram in i:
        print(i)

