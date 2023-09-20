import string


# def encrypting_message(message, key):
#     encrypted_message = ''
#     message = message.upper()
#     for i in range(len(message)):
#         if message[i].isalpha():
#             char_index = ord(message[i])
#             encrypted_index = char_index + key
#             if char_index + key > 90:
#                 rest_index = (char_index + key) - 90
#                 encrypted_index = 64 + rest_index
#             encrypted_message += chr(encrypted_index)
#         if not message[i].isalpha():
#             encrypted_message += message[i]
#     return encrypted_message
#
#
# def decrypting_message(message, key):
#     encrypted_message = ''
#     message = message.upper()
#     for i in range(len(message)):
#         if message[i].isalpha():
#             char_index = ord(message[i])
#             encrypted_index = char_index - key
#             if char_index - key < 65:
#                 rest_index = 90 - (64 - encrypted_index)
#                 encrypted_index = rest_index
#             encrypted_message += chr(encrypted_index)
#         if not message[i].isalpha():
#             encrypted_message += message[i]
#     return encrypted_message


def shift_letter(char, key):
    if char.isalpha():
        alphabet = string.ascii_uppercase if char.isupper() else string.ascii_lowercase
        index = alphabet.index(char)
        shifted_index = (index + key) % 26
        return alphabet[shifted_index]
    return char


def encrypt_message(message, key):
    encrypted_message = ''.join(shift_letter(char, key) for char in message)
    encrypted_message = encrypted_message.upper()
    return encrypted_message


def decrypt_message(message, key):
    encrypted_message = encrypt_message(message, -key)
    return encrypted_message.upper()


while True:
    choice = input('Do you want to (e)ncrypt or (d)ecrypt?\n').lower()
    if choice not in ("e", "d"):
        print('Please enter "e" for encrypt or "d" for decrypt')
        continue
    try:
        key = int(input('Please enter the key (0 to 25) to use.\n'))
        if not 0 <= key <= 25:
            print('Please enter a valid key in the range 0 to 25.')
            continue
        message = input('Enter the message to encrypt.\n')
        if choice == "e":
            result = encrypt_message(message, key)
        elif choice == "d":
            result = decrypt_message(message, key)
        print(result)

    except ValueError:
        print('Invalid input. Please enter numeric key.')
