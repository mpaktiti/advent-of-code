# TODO make the paths not relative cause they fail if run from the root
import sys; sys.path.insert(0, "../utils")
import utils

valid_symbols = "!@#$%^&*()_-+={}[]/"

# Input:
# - char: current digit being evaluated
# - engine_schematic: 2D array of all items
# - i: index of current row
# - j: index of current column
# - max_column_length: max number of columns in row (so I can avoid out of bounds errors when going right)
# Output:
# - whole_num: the initial number concatenated with the other digits found on its right
# - skip_counter: the number of digits found to the right of the current one so I can skip them
def get_number_going_right(char, engine_schematic, i, j, max_column_length):
    got_whole_num = False
    whole_num = char
    skip_counter = 1
    z = 1
    while not got_whole_num and j + z < max_column_length:
        if engine_schematic[i][j + z].isdigit():
            # print("skip counter is: ", skip_counter)
            skip_counter += 1
            whole_num = str(whole_num) + engine_schematic[i][j + z]
            z += 1
        else:
            got_whole_num = True
    return str(whole_num), skip_counter

# Input:
# - char: current digit being evaluated
# - engine_schematic: 2D array of all items
# - i: index of current row
# - j: index of current column
# Output:
# - whole_num: the initial number concatenated with the other digits found on its right
def get_number_going_left(char, engine_schematic, i, j):
    got_whole_num = False
    whole_num = char
    z = j - 1
    while not got_whole_num and z >= 0:
        if engine_schematic[i][z].isdigit():
            whole_num = engine_schematic[i][z] + whole_num
            z -= 1
        else:
            got_whole_num = True
    # print("whole number: ", whole_num)
    return str(whole_num)

# part 1: add up the part numbers
def part_one():
    # read file and copy characters to 2D array
    engine_schematic = []
    for line in utils.read_input():
        chars_array = []
        for char in line.strip():
            chars_array.append(char)
        engine_schematic.append(chars_array)

    # loop through array and sum the numbers that are adjacent to a symbol
    result, i = 0, 0
    while i < len(engine_schematic):
        j = 0
        max_column_length = len(engine_schematic[i])
        while j < max_column_length:
            char = engine_schematic[i][j]
            if char.isdigit():
                # print("Found digit: ", char)
                # Check for symbols up, down, left, and right, while staying within array bounds
                # if j is at the first line item I cannot check left (out of bounds)
                if j > 0:
                    if engine_schematic[i][j - 1] in valid_symbols:
                        # print(char, " has symbol left")
                        # get the whole num by reading the digits to the right
                        whole_num, skip_counter = get_number_going_right(char, engine_schematic, i, j, max_column_length)
                        # print("whole number: ", whole_num)
                        result += int(whole_num)
                        j += skip_counter
                        continue
                # if j is at the last line item I cannot check right (out of bounds)
                if j < max_column_length - 1:
                    if engine_schematic[i][j + 1] in valid_symbols:
                        # print(char, " has symbol right")
                        # get the whole num by reading the digits to the left
                        whole_num = get_number_going_left(char, engine_schematic, i, j)
                        result += int(whole_num)
                        j += 1
                        continue
                # UP SCENARIOS
                # if i is at the first row I cannot check any up scenarios (out of bounds)
                if i > 0:
                    if engine_schematic[i - 1][j - 1] in valid_symbols:
                        # print(char, " has symbol up left")
                        # if the symbol is up left I know that this is the first digit of the number
                        # so to get the whole num read the digits to the right
                        whole_num, skip_counter = get_number_going_right(char, engine_schematic, i, j, max_column_length)
                        # print("whole number: ", whole_num)
                        result += int(whole_num)
                        j += skip_counter
                        continue
                    elif engine_schematic[i - 1][j] in valid_symbols:
                        # print(char, " has symbol up")
                        # if the symbol is up then I cannot have a digit on my left
                        # because if I did it would have already found the symbol as up right
                        # so check for other digits only to the right
                        whole_num, skip_counter = get_number_going_right(char, engine_schematic, i, j, max_column_length)
                        # print("whole number: ", whole_num)
                        result += int(whole_num)
                        j += skip_counter
                        continue
                    elif j < max_column_length - 1:
                        if engine_schematic[i - 1][j + 1] in valid_symbols:
                            # print(char, " has symbol up right")
                            # I might have digits right or left, gotta check both sides
                            # first go left
                            whole_num = get_number_going_left(char, engine_schematic, i, j)
                            # print("whole num after going left: ", whole_num)
                            # then go right passing as input what you got from going left
                            whole_num, skip_counter = get_number_going_right(whole_num, engine_schematic, i, j, max_column_length)
                            # print("whole num after going right: ", whole_num)
                            result += int(whole_num)
                            # print("j: ", j)
                            # print("skip_counter: ", skip_counter)
                            j += skip_counter
                            # print("next column to check: ", j)
                            continue
                # DOWN SCENARIOS
                # if i is at the last row I cannot check any down scenarios (out of bounds)
                if i < len(engine_schematic) - 1:
                    if engine_schematic[i + 1][j - 1] in valid_symbols:
                        # print(char, " has symbol down left")
                        # if the symbol is down left I know that this is the first digit of the number
                        # so to get the whole num read the digits to the right
                        whole_num, skip_counter = get_number_going_right(char, engine_schematic, i, j, max_column_length)
                        # print("whole number: ", whole_num)
                        result += int(whole_num)
                        j += skip_counter
                        continue
                    elif engine_schematic[i + 1][j] in valid_symbols:
                        # print(char, " has symbol down")
                        # if the symbol is down then I cannot have a digit on my left
                        # because if I did it would have already found the symbol as down right
                        # so check for other digits only to the right
                        whole_num, skip_counter = get_number_going_right(char, engine_schematic, i, j, max_column_length)
                        # print("whole number: ", whole_num)
                        result += int(whole_num)
                        j += skip_counter
                        continue
                    elif j < max_column_length - 1:
                        if engine_schematic[i + 1][j + 1] in valid_symbols:
                            # print(char, " has symbol down right")
                            # I might have digits right or left, gotta check both sides
                            # first go left
                            whole_num = get_number_going_left(char, engine_schematic, i, j)
                            # print("whole num after going left: ", whole_num)
                            # then go right passing as input what you got from going left
                            whole_num, skip_counter = get_number_going_right(whole_num, engine_schematic, i, j, max_column_length)
                            # print("whole num after going right: ", whole_num)
                            result += int(whole_num)
                            j += skip_counter
                            continue
            j += 1
        i += 1
    return result

print("Sum of part numbers: ", part_one())