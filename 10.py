"""
 Write a function that takes camel-cased strings (i.e. ThisIsCamelCased), and converts them to snake case
 (i.e. this_is_camel_cased). Modify the function by adding an argument, separator, so it will also convert to
 the kebab case (i.e.this-is-camel-case) as well.
"""

import re


def snake_cased_separator(string_value, separator):
    result_list = []
    result_string = ''
    lis = re.findall('[A-Z][^A-Z]*', string_value)
    for i in lis:
        result_list.append(i.lower())
    result = list(map(lambda x: separator + x, result_list[1:]))
    result_list = [result_list[0]]
    result = result_list + result
    for i in result:
        result_string += i
    print(result_string)


string = input("Enter camel cased string:")
sep = input("Enter a separator:")
snake_cased_separator(string, sep)
