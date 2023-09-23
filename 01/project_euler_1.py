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

# 04
# largest_palindrome = 0
# for first_num in range(999, 101, -1):
#     for second_num in range(999, 101, -1):
#         product = first_num * second_num
#         if product == int(str(product)[::-1]) and product > largest_palindrome:
#             largest_palindrome = product
#             break
#
# print(largest_palindrome)

# 07
# def is_prime(number):
#     if number <= 1:
#         return False
#     elif number <= 3:
#         return True
#     elif number % 2 == 0 or number % 3 == 0:
#         return False
#     i = 5
#     while i * i <= number:
#         if number % i == 0 or number % (i + 2) == 0:
#             return False
#         i += 6
#     return True
#
#
# def find_nth_prime(nth):
#     prime_count = 0
#     candidate = 2
#     while True:
#         if is_prime(candidate):
#             prime_count += 1
#             if prime_count == nth:
#                 return candidate
#         candidate += 1
#
#
# n = 10001
# result = find_nth_prime(n)
# print(f"The {n}th prime number is: {result}")


# 06
# def sum_of_squares(n):
#     squares = [num ** 2 for num in range(n + 1)]
#     sum_squares = sum(squares)
#     return sum_squares
#
#
# def square_of_sum(n):
#     numbers = [num for num in range(n + 1)]
#     square_sum = (sum(numbers)) ** 2
#     return square_sum
#
#
# def find_difference(a, b):
#     return a - b
#
#
# n = 1000
# print(find_difference(square_of_sum(n), sum_of_squares(n)))


# 08
# def find_triplet(target):
#     for a in range(1, target):
#         for b in range(a + 1, target - a):
#             c = target - a - b
#             if a ** 2 + b ** 2 == c ** 2:
#                 return a, b, c
#
#
# def find_triplet_product(target):
#     triplet = find_triplet(target)
#     a, b, c = triplet
#     product = a * b * c
#     return product
#
#
# target = 1000
# print(find_triplet_product(1000))


# 09
# def is_prime(number):
#     if number <= 1:
#         return False
#     elif number <= 3:
#         return True
#     elif number % 2 == 0 or number % 3 == 0:
#         return False
#     i = 5
#     while i * i <= number:
#         if number % i == 0 or number % (i + 2) == 0:
#             return False
#         i += 6
#     return True
#
#
# def find_nth_prime(n):
#     prime_sum = 0
#     for i in range(2, n+1):
#         if is_prime(i):
#             prime_sum += i
#     return prime_sum
#
#
# n = 2000000
# print(find_nth_prime(n))


# 05
for i in range(1, 21):
    pass