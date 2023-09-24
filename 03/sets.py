# 01
# A = {1, 3, 7, 8}
# B = {6, 3, 1, 9}
#
# result = A.symmetric_difference(B)
# print(result)


# 02
# def is_prime(n):
#     if n <= 1:
#         return False
#     if n <= 3:
#         return True
#     if n % 2 == 0 or n % 3 == 0:
#         return False
#     i = 5
#     while i * i <= n:
#         if n % i == 0 or n % (i + 2) == 0:
#             return False
#         i += 6
#     return True
#
#
# def get_prime_numbers(list_of_numbers):
#     prime_numbers = set()
#     for num in list_of_numbers:
#         if is_prime(num):
#             prime_numbers.add(num)
#     return prime_numbers
#
#
# numbers = [18, 67, 49, 5, 34, 21, 87, 87, 4, 5, 34, 18]
# print(get_prime_numbers(numbers))

# 03
# def are_anagrams(first_word: str, second_word: str):
#     are_chars_same = False
#     for ch in first_word:
#         if ch in second_word:
#             second_word.replace(ch, '', 1)
#             are_chars_same = True
#         else:
#             return False
#     return are_chars_same
#
#
# def get_anagrams(list_of_words):
#     anagrams = set()
#     for word in list_of_words:
#         list_of_words.remove(word)
#         for compared_word in list_of_words:
#             if are_anagrams(word, compared_word):
#                 anagrams.add(word)
#                 anagrams.add(compared_word)
#                 list_of_words.remove(compared_word)
#     return anagrams
#
#
# words = ['rasp', 'hyf', 'spar', 'hook', 'kooh', 'huhgf', 'clock', 'colck']
# print(get_anagrams(words))

# 04
# from itertools import product
#
#
# def cartesian_product(sets):
#     if not sets:
#         return []
#     result = list(product(*sets))
#     return result
#
#
# first_set = {1, 2}
# second_set = {'A', 'B'}
# third_set = {True, False}
# list_of_sets = [first_set, second_set, third_set]
# print(cartesian_product(list_of_sets))


CHALLENGE_TOKEN = "w4zf51yeqa20"


def MathChallenge(num):
    if not (1 <= int(num) <= 1000):
        return "Invalid input, please enter a number between 1 and 1000."

    integer_num = int(num)
    for every_num in range(1, integer_num):
        integer_num += every_num
    num = str(integer_num)
    num += CHALLENGE_TOKEN
    for i in range(1, len(num) + 1):
        if i % 3 == 0:
            old_char = num[i - 1]
            num = num.replace(old_char, "X")
    return num


# keep this function call here
print(MathChallenge(input()))
