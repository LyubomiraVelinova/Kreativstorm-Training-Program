# 01
# data = []
#
# while True:
#     user_input = input()
#     if user_input == "done":
#         break
#     data.append(user_input)


# 02
# import random
#
# numbers = []
# while sum(numbers) <= 100:
#     number = random.randint(1, 10)
#     numbers.append(number)

# 03
# data = []
#
# while True:
#     user_input = input("Enter a string or 'exit' for exit: ")
#     if user_input == "exit":
#         break
#     elif user_input not in data:
#         data.append(user_input)
#         print(f'{user_input} is added to the list.')
#     else:
#         print('The string is not unique.')

# 04
# data = []
#
# while True:
#     user_input = input("Enter a number or 'exit' for exit: ")
#     if user_input == "exit":
#         break
#     elif int(user_input) >= 10:
#         data.append(int(user_input))
#     else:
#         print(f"{user_input} is less than 10.")

# 05
highest_number = 0

while True:
    user_input = input("Enter a number or 'done' for exit: ")
    if user_input == "done":
        print(f'Highest number is {highest_number}.')
        break
    elif int(user_input) > highest_number:
        highest_number = int(user_input)
