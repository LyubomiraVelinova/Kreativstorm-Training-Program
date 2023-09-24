# 01
# from collections import Counter
#
#
# def get_most_common_elements(input_tuple):
#     elements = Counter(input_tuple)
#     most_common = elements.most_common()
#     max_count = most_common[0][1]
#     most_common_elements = [el for el, count in most_common if max_count == count]
#     return most_common_elements
#
#
# data = (1, 5, 8, 5, 8, 3, 0, 4, 5)
# result = get_most_common_elements(data)
# print(result)

# 02
# def is_palindrome(input_tuple):
#     are_equal = False
#     for i in range(len(input_tuple)//2):
#         if input_tuple[i] == input_tuple[-(i + 1)]:
#             are_equal = True
#         else:
#             are_equal = False
#             break
#     return are_equal
#
#
# data = (1, 2, 3, 4, 5, 5, 4, 3, 2, 1)
# print(is_palindrome(data))

# 03
# from collections import defaultdict
#
#
# def get_elements_frequency(input_tuple):
#     elements_frequency = defaultdict(int)
#     for el in input_tuple:
#         elements_frequency[el] += 1
#     return elements_frequency
#
#
# data = (1, 6, 3, 4, 5, 5, 9, 3, 6, 1)
# print(get_elements_frequency(data))

# 04
# def get_even_elements(input_tuple):
#     new_tuple = tuple(el for el in input_tuple if el % 2 == 0)
#     return new_tuple
#
#
# data = (1, 6, 3, 4, 5, 5, 9, 3, 6, 1)
# print(get_even_elements(data))

# 05
def get_unique_elements(input_tuple):
    unique_elements = tuple(el for el in input_tuple if input_tuple.count(el) == 1)
    return unique_elements


data = (1, 6, 3, 4, 5, 5, 9, 3, 6, 1)
print(get_unique_elements(data))
