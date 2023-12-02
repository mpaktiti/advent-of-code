import re

# read file into memory
with open("01-input.txt") as input_file:
    file_data = input_file.readlines()


# iterate over the items and calculate the sum for part 1
sum = 0
for line in file_data:
    digits_found = []
    for char in line:
        if char in '0123456789':
            digits_found.append(char)
    if len(digits_found) >= 2:
        sum += int(digits_found[0] + digits_found[-1])
    else:
        sum += int(digits_found[0] + digits_found[0])

print("Part 1 SUM: ", sum)

# iterate over the items and calculate the sum for part 2
sum = 0
for line in file_data:
    # check if the line contains digit numbers
    char_index = 0
    digits_found = {}
    for char in line:
        if char in '0123456789':
            digits_found[char_index] = char
        char_index += 1

    # check if the line contains word numbers
    numbers = {"1": "one", "2": "two", "3": "three", "4": "four", "5": "five", "6": "six", "7": "seven", "8": "eight", "9": "nine"}
    for key in numbers:
        indexes_of_number = [m.start() for m in re.finditer(numbers[key], line)]
        if len(indexes_of_number) >= 1:
            for i in indexes_of_number:
                digits_found[i] = key

    # sort the dictionary according to index
    sorted_dict = dict(sorted(digits_found.items()))

    # do the sum of the first and last digits
    first_item = list(sorted_dict)[0]
    if len(sorted_dict) >= 2:
        last_item = list(sorted_dict)[-1]
        sum += int(sorted_dict[first_item] + sorted_dict[last_item])
    else:
        sum += int(sorted_dict[first_item] + sorted_dict[first_item])

print("Part 2 SUM: ", sum)