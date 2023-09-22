# 01
with open('readme.txt') as f:
    lines = f.readlines()
    lines_number = len(lines)
    words_number = 0
    characters_number = 0
    for line in lines:
        for word in line.split(' '):
            words_number += 1
            for char in word:
                if char.isalpha():
                    characters_number += 1

    print(lines_number, words_number, characters_number)


# 02
import csv

data_dict = {}
with open("data.csv", 'r') as file:
    reader = csv.DictReader(file)

    for row in reader:
        data_dict[row['Name']] = {'Age': row['Age'], 'Location': row['Location']}

print(data_dict)

# 03
with open('binary.bin', 'rb') as binary_file:
    binary_data = binary_file.read()

hexadecimal_string = binary_data.hex()

with open('hexadecimal_output.txt', 'w') as text_file:
    text_file.write(hexadecimal_string)

# 04
with open('numbers.txt', 'r') as f:
    lines = f.readlines()
    numbers_list = [int(line) for line in lines]
    print(sum(numbers_list))

# 05
file_name = 'readme.txt'
with open(file_name, 'r') as f:
    lines = f.readlines()
    new_text = []
    for line in lines:
        if line != '\n':
            new_text.append(line)


with open(file_name, 'w') as f:
    f.writelines(''.join(new_text))
