map = {}

# open file and return contents to caller
def read_input():
    with open("input.txt") as input_file:
        return input_file.readlines()

# read cards from file and copy them to memory
def read_cards():
    is_first_line = True
    for line in read_input():
        if is_first_line:
            instructions = line.strip()
            is_first_line = False
            continue
        elif line.isspace():
            continue
        temp = line.strip().split('=')
        remove_parenthesis = temp[1].strip()[1:-1]
        temp2 = remove_parenthesis.strip().split(',')
        map[temp[0].strip()] = [temp2[0].strip(), temp2[1].strip()]
    return instructions

def read_map(instructions):
    current_pos = 'AAA'
    target_pos = 'ZZZ'
    steps_taken = 0
    i = 0
    while current_pos != target_pos:
        direction = instructions[i]
        i += 1
        if i == len(instructions): # if you ran out of instructions repeat the same
            i = 0
        if direction == 'L':
            current_pos = map[current_pos][0]
        else:
            current_pos = map[current_pos][1]
        steps_taken += 1
    return steps_taken

instructions = read_cards()
print('number of steps to reach ZZZ: ', read_map(instructions))