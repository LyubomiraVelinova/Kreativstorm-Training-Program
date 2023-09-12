'''
Write a program that prompts the user for a string
and checks whether the string is a palindrome (i.e., the string reads the same forward and backward).
'''

# def is_palindrome(text: str):
#     return text == text[::-1]
#
#
# user_input = input("Enter a string: ")
#
# print(is_palindrome(user_input))

'''
Write a program that takes in a list of integers 
and returns the sum of all even numbers in the list.
'''

# def get_even_numbers(numbers: list):
#     even_nums = [num for num in numbers if num % 2 == 0]
#     return sum(even_nums)
#
#
# print(get_even_numbers([2, 4, 7, 8]))

'''
Write a program that prompts the user for their age 
and checks whether they are old enough to vote (i.e., 18 years old or older).
'''

# age = input("Enter your age: ")
# try:
#     age = int(age)
#     if age >= 18:
#         print('You are old enough to vote.')
#     else:
#         print('You are not old enough to vote.')
# except ValueError:
#     print("Invalid input. Please enter a valid age as a number.")

'''
Write a program that takes in a list of integers 
and returns the largest number in the list that is also divisible by 3.
'''

# def finding_largest_num_divisible_by_three(numbers: list):
#     divisible_by_three_nums = [num for num in numbers if num % 3 == 0]
#     sorted_divisible_by_three_nums = sorted(divisible_by_three_nums, reverse=True)
#     return sorted_divisible_by_three_nums[0]
#
#
# print(finding_largest_num_divisible_by_three([1, 4, 8, 9, 37]))


'''
Write a program that prompts the user for a number 
and checks whether the number is a prime number (i.e., only divisible by 1 and itself).
'''


def is_prime_num(num):
    if num <= 1:
        return False
    elif num <= 3:
        return True
    elif num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True


user_input = int(input("Enter a number: "))

try:
    if is_prime_num(user_input):
        print(f'{user_input} is a prime number.')
    else:
        print(f'{user_input} is not a prime number.')
except ValueError:
    print("Invalid data. Please, insert a valid number.")
