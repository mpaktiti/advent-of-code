maze = []
can_go_left_chars = 'LF-'
can_go_right_chars = '7J-'
can_go_up_chars = '7F|'
can_go_down_chars = 'JL|'

def read_maze():
    file = open('input.txt').readlines()
    for line in file:
        maze.append([char for char in line.strip()])
    # maze = [[char for char in line.strip()] for line in file]

# find starting point
def find_starting_point():
    starting_point = []
    for i in range(0, len(maze)):
        for j in range(0,len(maze[i])):
            if maze[i][j] == 'S':
                starting_point = [i,j]
                break
            if len(starting_point) > 0 : break
    return starting_point

def print_maze():
    for i in range(0, len(maze)-1):
        cols = ''
        for col in maze[i]:
            cols += col
        print(cols)

def check_left(row, col, element):
    if col > 0: # stay within bounds
        # print('character on the left is ', maze[row][col-1])
        if maze[row][col-1][-1] != '!' and maze[row][col-1] in can_go_left_chars: # check if the element has already been passed
            # print('going left')
            maze[row][col] = element + "!"
            col -= 1
    return col

def check_right(row, col, element):
    if col < len(maze[0]) - 1: # stay within bounds
        # print('character on the right is ', maze[row][col+1])
        if maze[row][col+1][-1] != '!' and maze[row][col+1] in can_go_right_chars:
            # print('going right')
            maze[row][col] = element + "!"
            col += 1
    return col

def check_up(row, col, element):
    if row > 0:
        # print('character up is ', maze[row-1][col])
        if maze[row-1][col][-1] != '!' and maze[row-1][col] in can_go_up_chars:
            # print('going up')
            maze[row][col] = element + "!"
            row -= 1
    return row

def check_down(row, col, element):
    if row < len(maze) - 1:
        # print('character down is ', maze[row+1][col])
        if maze[row+1][col][-1] != '!' and maze[row+1][col] in can_go_down_chars:
            # print('going down')
            maze[row][col] = element + "!"
            row += 1 
    return row

def run_all_checks_for_entrypoint(next_check_for_s, row, col, element, directions, i):
    # left
    if next_check_for_s == 0:
        # print('checking on the left of S')
        new_col = check_left(row, col, element)
        if new_col != col: # if I can move left
            # print('updated direction: ', [row, new_col])
            return next_check_for_s+1, [row, new_col], row, new_col
        next_check_for_s +=1
    
    #right
    if next_check_for_s == 1:
        # print('checking on the right of S')
        new_col = check_right(row, col, element)
        if new_col != col: # if I can move right
            # print('updated direction: ', [row, new_col])
            return next_check_for_s+1, [row, new_col], row, new_col
        next_check_for_s += 1
    
    # up
    if next_check_for_s == 2:
        # print('checking up of S')
        new_row = check_up(row, col, element)
        if new_row != row: # if I can move up
            # print('updated direction: ', [new_row, col])
            return next_check_for_s + 1, [new_row, col], new_row, col
        next_check_for_s +=1
    
    # down
    if next_check_for_s == 3:
        # print('checking down of S')
        new_row = check_down(row, col, element)
        if new_row != row: # if I can move down
            # print('updated direction: ', [new_row, col])
            return next_check_for_s + 1, [new_row, col], new_row, col
        next_check_for_s +=1
    
    return next_check_for_s, directions[i], row, col

def find_next_step(directions):
    # print('find_next_step input directions: ', directions)    
    entry_point = False
    next_check_for_s = 0
    for i in range(0, len(directions)):
        direction = directions[i]
        # print('checking direction: ', direction)
        row = direction[0] # direction[0] = 1
        col = direction[1] # direction[1] = 2
        element = maze[row][col]
        # print('element is ', element)
        if element == 'S' or (element == 'S!' and entry_point):
            entry_point = not entry_point
            next_check_for_s, directions[i], row, col = run_all_checks_for_entrypoint(next_check_for_s, row, col, element, directions, i)
            # print('next_check_for_s: ', next_check_for_s)
        elif element == '-': # go left or right
                new_col = check_left(row, col, element)
                if new_col == col: # if it didn't move left
                    new_col = check_right(row, col, element)
                col = new_col
        elif element == '|': # go up or down
            new_row = check_up(row, col, element)
            if new_row == row: # if it didn't move up
                new_row = check_down(row, col, element)
            row = new_row
        elif element == 'F': # go left or down
            new_col = check_right(row, col, element)
            row = check_down(row, col, element)
            col = new_col
        elif element == '7': # go left or down
            new_col = check_left(row, col, element)
            row = check_down(row, col, element)
            col = new_col
        elif element == 'J': # go left or down
            new_col = check_left(row, col, element)
            row = check_up(row, col, element)
            col = new_col
        elif element == 'L': # go left or down
            new_col = check_right(row, col, element)
            row = check_up(row, col, element)
            col = new_col
        directions[i] = [row, col]
        # print('updated direction: ', directions[i])
    return directions

def part_one():
    starting_point = find_starting_point()
    print('starting point is at ', starting_point)

    steps = 0
    directions = [starting_point, starting_point]
    while True:
        directions = find_next_step(directions)
        steps += 1
        if directions[0] == directions[1] : break
    return steps


def part_two():
    enclosed_tiles = 0
    dots = 0
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == '.':
                dots += 1
    print('num of dots: ', dots)
    return enclosed_tiles

read_maze()
print_maze()
print('num of steps: ', part_one())
print('num of enclosed tiles: ', part_two())
