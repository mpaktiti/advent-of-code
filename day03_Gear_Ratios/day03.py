valid_symbols = "!@#$%^&*()_-+={}[]/"
part_numbers = {}

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
    if char.isdigit():
        whole_num = char
    else:
        whole_num = ''
    skip_counter = 1
    z = 1
    while not got_whole_num and j + z < max_column_length:
        if engine_schematic[i][j + z].isdigit():
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
    if char.isdigit():
        whole_num = char
    else:
        whole_num = ''
    z = j - 1
    counter_left = 0
    while not got_whole_num and z >= 0:
        if engine_schematic[i][z].isdigit():
            whole_num = engine_schematic[i][z] + whole_num
            counter_left += 1
            z -= 1
        else:
            got_whole_num = True
    return str(whole_num), counter_left

def build_array_from_file():
    engine_schematic = []
    for line in open("input.txt").readlines():
        chars_array = [char for char in line.strip()]
        engine_schematic.append(chars_array)
    return engine_schematic

# part 1: add up the part numbers
def part_one():
    # read file and copy characters to 2D array
    engine_schematic = build_array_from_file()

    # loop through array and sum the numbers that are adjacent to a symbol
    for i in range(0, len(engine_schematic)):
        j = 0
        max_column_length = len(engine_schematic[i])
        while j < max_column_length:
            char = engine_schematic[i][j]
            if char.isdigit():
                # Check for symbols up, down, left, and right, while staying within array bounds
                # if j is at the first line item I cannot check left (out of bounds)
                if j > 0:
                    if engine_schematic[i][j - 1] in valid_symbols:
                        # has symbol left
                        # get the whole num by reading the digits to the right
                        whole_num, skip_counter = get_number_going_right(char, engine_schematic, i, j, max_column_length)
                        part_numbers[str(i) + "," + str(j)] = whole_num
                        j += skip_counter
                        continue
                # if j is at the last line item I cannot check right (out of bounds)
                if j < max_column_length - 1:
                    if engine_schematic[i][j + 1] in valid_symbols:
                        # has symbol right
                        # get the whole num by reading the digits to the left
                        whole_num, counter_left = get_number_going_left(char, engine_schematic, i, j)
                        whole_num_position = j-counter_left # calc the column of the number's first digit
                        part_numbers[str(i) + "," + str(whole_num_position)] = whole_num
                        j += 1
                        continue
                # UP SCENARIOS
                # if i is at the first row I cannot check any up scenarios (out of bounds)
                if i > 0:
                    if engine_schematic[i - 1][j - 1] in valid_symbols:
                        # if the symbol is up left I know that this is the first digit of the number
                        # so to get the whole num read the digits to the right
                        whole_num, skip_counter = get_number_going_right(char, engine_schematic, i, j, max_column_length)
                        part_numbers[str(i) + "," + str(j)] = whole_num
                        j += skip_counter
                        continue
                    elif engine_schematic[i - 1][j] in valid_symbols:
                        # if the symbol is up then I cannot have a digit on my left
                        # because if I did it would have already found the symbol as up right
                        # so check for other digits only to the right
                        whole_num, skip_counter = get_number_going_right(char, engine_schematic, i, j, max_column_length)
                        part_numbers[str(i) + "," + str(j)] = whole_num
                        j += skip_counter
                        continue
                    elif j < max_column_length - 1:
                        if engine_schematic[i - 1][j + 1] in valid_symbols:
                            # found symbol up right
                            # I might have digits right or left, gotta check both sides
                            # first go left
                            whole_num, counter_left = get_number_going_left(char, engine_schematic, i, j)
                            # then go right passing as input what you got from going left
                            whole_num, skip_counter = get_number_going_right(whole_num, engine_schematic, i, j, max_column_length)
                            whole_num_position = j-counter_left # calc the column of the number's first digit
                            part_numbers[str(i) + "," + str(whole_num_position)] = whole_num
                            j += skip_counter
                            continue
                # DOWN SCENARIOS
                # if i is at the last row I cannot check any down scenarios (out of bounds)
                if i < len(engine_schematic) - 1:
                    if engine_schematic[i + 1][j - 1] in valid_symbols:
                        # if the symbol is down left I know that this is the first digit of the number
                        # so to get the whole num read the digits to the right
                        whole_num, skip_counter = get_number_going_right(char, engine_schematic, i, j, max_column_length)
                        part_numbers[str(i) + "," + str(j)] = whole_num
                        j += skip_counter
                        continue
                    elif engine_schematic[i + 1][j] in valid_symbols:
                        # if the symbol is down then I cannot have a digit on my left
                        # because if I did it would have already found the symbol as down right
                        # so check for other digits only to the right
                        whole_num, skip_counter = get_number_going_right(char, engine_schematic, i, j, max_column_length)
                        part_numbers[str(i) + "," + str(j)] = whole_num
                        j += skip_counter
                        continue
                    elif j < max_column_length - 1:
                        if engine_schematic[i + 1][j + 1] in valid_symbols:
                            # I might have digits right or left, gotta check both sides
                            # first go left
                            whole_num, counter_left = get_number_going_left(char, engine_schematic, i, j)
                            # then go right passing as input what you got from going left
                            whole_num, skip_counter = get_number_going_right(whole_num, engine_schematic, i, j, max_column_length)
                            whole_num_position = j-counter_left # calc the column of the number's first digit
                            part_numbers[str(i) + "," + str(whole_num_position)] = whole_num
                            j += skip_counter
                            continue
            j += 1
    result = sum([int(item) for item in part_numbers.values()])
    return result

def is_part_number(whole_num, i, j):
    key = str(i) + "," + str(j)
    if key in part_numbers:
        return part_numbers[key] == whole_num

def part_two():
    # read file and copy characters to 2D array
    engine_schematic = build_array_from_file()

    # loop through array and find the symbols adjacent to two numbers
    result = 0
    for i in range(0, len(engine_schematic)):
        max_column_length = len(engine_schematic[i])
        for j in range(0, max_column_length):
            char = engine_schematic[i][j]
            nums_found = []
            whole_num = ''
            up_left_j, down_left_j = -1, -1
            if char == '*':
                # Check for numbers up, down, left, and right, while staying within array bounds
                # if j is at the first line item I cannot check left (out of bounds)
                if j > 0:
                    # check if there is a number to the left
                    if engine_schematic[i][j - 1].isdigit():
                        # has number left
                        # get the whole num by reading the digits to the left
                        whole_num, counter_left = get_number_going_left(char, engine_schematic, i, j)
                        if is_part_number(whole_num, i, j-counter_left):
                            nums_found.append(int(whole_num))
                        whole_num = ''
                # if j is at the last line item I cannot check right (out of bounds)
                if j < max_column_length - 1:
                    # check if there is a number to the right
                    if engine_schematic[i][j + 1].isdigit():
                        # has number right
                        # get the whole num by reading the digits to the right
                        whole_num, _ = get_number_going_right(char, engine_schematic, i, j, max_column_length)
                        if is_part_number(whole_num, i, j+1):
                            nums_found.append(int(whole_num))
                        whole_num = ''
                # UP SCENARIOS
                # if i is at the first row I cannot check any up scenarios (out of bounds)
                if i > 0:
                    if engine_schematic[i - 1][j - 1].isdigit():
                        # if the number is up left I have to check both to its left and its right
                        # first go left
                        whole_num, counter_left = get_number_going_left(char, engine_schematic, i-1, j)
                        # then go right passing as input what you got from going left
                        whole_num, _ = get_number_going_right(whole_num, engine_schematic, i-1, j-1, max_column_length)
                        if is_part_number(whole_num, i-1, j-counter_left):
                            nums_found.append(int(whole_num))
                            up_left_j = j-counter_left
                        whole_num = ''
                    if engine_schematic[i - 1][j].isdigit():
                        # has number up
                        # I have already checked up left so go only right
                        whole_num, _ = get_number_going_right(char, engine_schematic, i-1, j-1, max_column_length)
                        if is_part_number(whole_num, i-1, j):
                            nums_found.append(int(whole_num))
                        whole_num = ''
                    if j < max_column_length - 1:
                        if engine_schematic[i - 1][j + 1].isdigit():
                            # I have already checked up left so go only right
                            whole_num, _ = get_number_going_right(whole_num, engine_schematic, i-1, j, max_column_length)
                            if up_left_j != j+1:
                                if is_part_number(whole_num, i-1, j+1):
                                    nums_found.append(int(whole_num))
                            whole_num = ''
                # DOWN SCENARIOS
                # if i is at the last row I cannot check any down scenarios (out of bounds)
                if i < len(engine_schematic) - 1:
                    if engine_schematic[i + 1][j - 1].isdigit():
                        # if the number is down left I have to check both to its left and its right
                        # first go left
                        whole_num, counter_left = get_number_going_left(char, engine_schematic, i+1, j)
                        # then go right passing as input what you got from going left
                        whole_num, skip_counter = get_number_going_right(whole_num, engine_schematic, i+1, j-1, max_column_length)
                        if is_part_number(whole_num, i+1, j-counter_left):
                            nums_found.append(int(whole_num))
                            down_left_j = j-counter_left
                        whole_num = ''
                    if engine_schematic[i + 1][j].isdigit():
                        # I have already checked down left so go only right
                        whole_num, skip_counter = get_number_going_right(char, engine_schematic, i+1, j-1, max_column_length)
                        if is_part_number(whole_num, i+1, j):
                            nums_found.append(int(whole_num))
                        whole_num = ''
                    if j < max_column_length - 1:
                        if engine_schematic[i + 1][j + 1].isdigit():
                            # number down right
                            # I have already checked up left so go only right
                            whole_num, skip_counter = get_number_going_right(whole_num, engine_schematic, i+1, j, max_column_length)
                            if down_left_j != j+1:
                                if is_part_number(whole_num, i+1, j+1):
                                    nums_found.append(int(whole_num))
            if len(nums_found) == 2:
                result += nums_found[0] * nums_found[1]
    return result

print("Sum of part numbers: ", part_one())
print("Sum of all of the gear ratios: ", part_two())