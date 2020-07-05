"""
Write a function to write a comma-separated value (CSV) file. It should accept a filename and a list of tuples as
parameters. The tuples should have a name, address, and age. The file should create a header row followed by a row for
each tuple. If the following list of tuples was passed in: [('George', '4312 Abbey Road', 22), ('John', '54 Love Ave',
21)] it should write the following in the file:
name,address,age George,4312 Abbey Road,22
John,54 Love Ave,21
"""
import csv


def comma_separate_accept(filename, parameter_list):
    header = ("Name", "address", "age")
    with open(filename, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=header)
        writer.writeheader()

        writer = csv.writer(file)
        writer.writerow(header)
        for i in parameter_list:
            writer.writerow(i)


lis = [('George', '4312 Abbey Road', 22), ('John', '54 Love Ave', 21)]
comma_separate_accept('hello.csv', lis)
