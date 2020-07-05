"""
Write a program that serves as a basic calculator. It asks for two numbers, then it asks for an operator.
 Gracefully deal with input that doesn't cleanly convert to numbers. Deal with division by zero errors.
"""

try:
    first_input = int(input("Enter First Number:"))
    second_input  = int(input("Enter second number:"))
except ValueError:
    print("Please insert numbers as instructed")
operator = input("Enter the operator: ")
if operator == '+':
    print(f'The sum is {first_input + second_input}')
elif operator == '-':
    print(f'The difference is {first_input - second_input}')
elif operator == "*":
    print(f'The product is {first_input * second_input}')
elif operator == "/":
    try:
        print(f'The quotient is {first_input/ second_input}')
    except ZeroDivisionError:
        print("Divide by zero gives infinity ")
else:
    print("Please enter a valid operator")

