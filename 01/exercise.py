# hours = int(input('Enter Hours:'))
# rate = float(input('Enter Rate:'))
# print(f'Pay:{hours * rate}')

def maximumOccurringCharacter(text):
    chars = {}
    text_len = len(text)

    for i in range(text_len):
        current_char = text[i]
        if current_char in chars:
            chars[current_char] += 1
        else:
            chars[current_char] = 1
        #
        # if count < chars[current_char]:
        #     count = chars[current_char]
        #     result = current_char

    count = 0
    result = ''

    for key, value in chars.items():
        if value > count:
            count = value
            result = key

    return result


maximumOccurringCharacter('hellowoorld')
