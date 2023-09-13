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

# def strings_to_float(numbers: list):
#     result = []
#     for char in numbers:
#         try:
#             result.append(float(char))
#         except ValueError:
#             pass
#
#     return result
#
#
# user_input = input("Enter list of strings, separated by comma and space: ")
# list_input = user_input.split(', ')
# print(strings_to_float(list_input))


'''
Write a function that takes a list of dictionaries as an argument, and returns the value of a specified key from each dictionary. 
Use a try-except block to catch any KeyError exceptions that may be raised when attempting to access a key that does not exist in a dictionary.
'''

# def get_values_from_dicts(dicts, key):
#     values = []
#     for d in dicts:
#         try:
#             value = d[key]
#             values.append(value)
#         except KeyError:
#             pass
#
#     return values
#
#
# dict_list = [
#     {'name': 'Lyuba', 'age': 30},
#     {'name': 'Brave', 'age': 25},
#     {'name': 'Huston'},
# ]
#
# key_to_extract = 'age'
# print(get_values_from_dicts(dict_list, key_to_extract))


'''
Write a function that takes a list of integers as an argument, and returns the largest integer in the list. 
Use a try-except block to catch any ValueError exceptions that may be raised when attempting to compare elements that are not integers.
'''


def get_largest_integer(numbers: list):
    largest_int = None

    for char in numbers:
        try:
            if largest_int is None or int(char) > largest_int:
                largest_int = int(char)
        except ValueError:
            pass
    return largest_int


user_input = input("Enter a list of integers, separated with comma and space: ")
list_input = user_input.split(', ')
print(get_largest_integer(list_input))
