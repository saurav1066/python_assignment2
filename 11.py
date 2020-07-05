"""
 Create a variable, filename. Assuming that it has a three-letter extension, and using slice operations,
 find the extension. For README.txt, the extension should be txt. Write code using slice operations that will
  give the name without the extension. Does your code work on filenames of arbitrary length?
"""

inp = input("Enter filename:")
index = inp.find('.')
[name,extension] = inp[:index], inp[index:]
if extension == '.txt':
    print(name)
else:
    print("Not valid")