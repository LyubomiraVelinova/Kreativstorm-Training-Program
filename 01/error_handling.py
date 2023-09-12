'''
Write a function that takes a list of integers as an argument, and returns the sum of the integers.
Use a try-except block to catch any ValueError exceptions that may be raised when attempting to convert a string to an integer.
'''

# def integers_sum(numbers: list):
#     numbers_sum = 0
#     for num in numbers:
#         numbers_sum += num
#     return numbers_sum
#
#
# user_input = input("Enter a list of integers, separated by comma and spaces: ")
# input_list = user_input.split(', ')
#
# try:
#     int_list = list(map(int, input_list))
#     print(integers_sum(int_list))
# except ValueError:
#     print("Invalid data!")


'''
Write a function that takes a filename as an argument, and attempts to open the file. Use a try-except block to catch any FileNotFoundError exceptions that may be raised when attempting to open the file. 
If the file is successfully opened, the function should return the contents of the file.
'''


# def read_file(filename):
#     try:
#         with open(filename, 'r') as file:
#             contents = file.read()
#         return contents
#     except FileNotFoundError:
#         return f'The file {filename} was not found.'
#
#
# filename = "example.txt"
# print(read_file(filename))


'''
Write a function that takes a list of strings as an argument, and returns a new list containing only the strings that can be successfully converted to a float. 
Use a try-except block to catch any ValueError exceptions that may be raised when attempting to convert a string to a float.
'''