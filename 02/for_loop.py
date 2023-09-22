# 01
# chars = input('Enter strings, separated by space: ').split(' ')
#
# for char in chars:
#     print(char.upper())

# 02
# numbers = [int(num) for num in input('Enter numbers, separated by space: ').split(' ')]
#
# for num in numbers:
#     print(num * num)


# 03
# list_of_dictionaries = [
#     {'1': 'first'},
#     {'2': 'second'},
#     {'3': 'third'},
# ]
#
# for every_dict in list_of_dictionaries:
#     for key in every_dict.keys():
#         print(key)

# 04
# numbers = [2, 4, 5, 7, 8]
#
# largest_num = 0
# for num in numbers:
#     if num > 0:
#         largest_num = num
#
# print(largest_num)

# 05
matrix = [[2, 4], [5, 7], [8, 22]]
for sublist in matrix:
    print(sum(sublist))
