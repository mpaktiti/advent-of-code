import re
import math

# read cards from file and copy them to memory
def read_cards():
    desert_map = {}
    file = open("input.txt").readlines() # TODO replace read_input() with this
    instructions = list(file[0].strip()) # first line is instructions
    # 3+ lines are the desert map nodes
    desert_map = {
        x[1]: (x[2], x[3])
        for x in (re.match(r"(\w+)\s*=\s*\((\w+), (\w+)\)", line) for line in file[2:])
    }
    return instructions, desert_map

def read_map_as_human(instructions, desert_map, current_pos):
    steps_taken = 0
    i = 0
    condition = True
    while condition:
        direction = instructions[i]
        i += 1
        if i == len(instructions): # if you ran out of instructions repeat the same
            i = 0
        current_pos = desert_map[current_pos][direction == 'R']
        steps_taken += 1
        condition = current_pos != 'ZZZ' if current_pos == 'AAA' else not current_pos.endswith("Z")
    return steps_taken

def read_map_as_ghost(instructions, desert_map):
    count = []
    for next_node in [n for n in desert_map if n.endswith("A")]:
        steps_for_next_node = read_map_as_human(instructions, desert_map, next_node)
        count.append(steps_for_next_node)
    return math.lcm(*count)

instructions, desert_map = read_cards()
print('number of human steps to reach ZZZ: ', read_map_as_human(instructions, desert_map, 'AAA'))
print('number of ghost steps to reach ZZZ: ', read_map_as_ghost(instructions, desert_map))
