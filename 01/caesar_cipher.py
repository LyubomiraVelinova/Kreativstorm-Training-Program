def encrypting_message(message, key):
    encrypted_message = ''
    message = message.upper()
    for i in range(len(message)):
        if message[i].isalpha():
            char_index = ord(message[i])
            encrypted_index = char_index + key
            if char_index + key > 90:
                rest_index = (char_index + key) - 90
                encrypted_index = 64 + rest_index
            encrypted_message += chr(encrypted_index)
        if not message[i].isalpha():
            encrypted_message += message[i]
    return encrypted_message


def decrypting_message(message, key):
    encrypted_message = ''
    message = message.upper()
    for i in range(len(message)):
        if message[i].isalpha():
            char_index = ord(message[i])
            encrypted_index = char_index - key
            if char_index - key < 65:
                rest_index = 90 - (64 - encrypted_index)
                encrypted_index = rest_index
            encrypted_message += chr(encrypted_index)
        if not message[i].isalpha():
            encrypted_message += message[i]
    return encrypted_message


encrypt_or_decrypt = input('Do you want to (e)ncrypt or (d)ecrypt?\n')
try:
    if encrypt_or_decrypt == 'e':
        number = int(input('Please enter the key (0 to 25) to use.\n'))
        message = input('Enter the message to encrypt.\n')
        print(encrypting_message(message, number))
    elif encrypt_or_decrypt == 'd':
        number = int(input('Please enter the key (0 to 26) to use.\n'))
        message = input('Enter the message to decrypt.\n')
        print(decrypting_message(message, number))
except ValueError:
    print('Please enter "e" for encrypt or "d" for decrypt')
