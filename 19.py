"""
Write a Python class to find validity of a string of parentheses, '(', ')', '{', '}', '[' and '].
These brackets must be close in the correct order, for example "()" and "()[]{}" are valid but "[)", "({[)]" and "{{{"
are invalid
"""


class CheckParentheis:
    opening_brackets = ["[", "{", "("]
    closing_brackets = ["]", "}", ")"]
    stack = []
    string = input("Enter the parenthesis:")
    for i in string:
        if i in opening_brackets:
            stack.append(i)
        elif i in closing_brackets:
            pos = closing_brackets.index(i)
            if ((len(stack) > 0) and
                    (opening_brackets[pos] == stack[len(stack) - 1])):
                stack.pop()
            else:
                print("Unbalanced")
    if len(stack) == 0:
        print("Balanced")
