# 01
# total_sum = sum([num for num in range(1, 1001) if num % 3 == 0 or num % 5 == 0])
#
# print(total_sum)

# 02
# def even_fibonacci_sum(limit):
#     a, b = 1, 2
#     even_sum = 0
#
#     while a <= limit:
#         if a % 2 == 0:
#             even_sum += a
#
#         a, b = b, a + b
#
#     return even_sum
#
#
# limit = 4000000
# print(even_fibonacci_sum(limit))

# 03
# def largest_prime_factory(number):
#     i = 2
#     while i * i <= number:
#         if number % i != 0:
#             i += 1
#         else:
#             number //= i
#     return number
#
#
# print(largest_prime_factory(600851475143))

# 05
# number = 1
#
# biggest_number = 1
# for num in range(1, 21):
#     biggest_number *= num
#
# print(biggest_number)


# def find_num(biggest_number):
#     num = 1
#     divisors = []
#     while num <= 20:
#         if biggest_number % num == 0:
#             divisors.append(num)
#             biggest_number //= num
#         num += 1
#
#     result = 1
#     for num in divisors:
#         result *= num
#
#     return biggest_number * result
#
#
# print(find_num(biggest_number))

from functools import reduce

numbers = [1, 5, 7, 9]
total = reduce(lambda x, y: x + y, numbers)
average = total / len(numbers)

print(averag)
