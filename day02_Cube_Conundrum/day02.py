valid_cubes = {'green': 13, 'red': 12, 'blue': 14}

def draw_is_impossible(games):
    for key in valid_cubes:
        if games.get(key) is not None:
            if games[key] > valid_cubes[key]:
                return True
    return False

# part 1: check which games are valid
def part_one(file):
    result = 0
    for line in file:
        split_by_semicolon = line.split(":")
        draws = split_by_semicolon[1].strip().split(";")
        games = {}
        impossible_draw = False
        # loop through draws, convert each one into a dict and check if the values are within bounds
        for draw in draws:
            # convert draw string to dict
            split_by_game = draw.split(",")
            for game in split_by_game:
                split_by_space = game.split()
                games[split_by_space[1]] = int(split_by_space[0])
            # check if draw is within bounds, if not the game is not possible so don't check the other draws
            if draw_is_impossible(games):
                impossible_draw = True
                break;
        # if impossible_draw is still False then all draws were within bounds
        if not impossible_draw:
            game_id = split_by_semicolon[0].split()
            result += int(game_id[1])
    return result

# part 2: check the minimum number of cubes required per game and calculate the power
def part_two(file):
    result = 0
    file = open("input.txt").readlines()
    for line in file:
        split_by_semicolon = line.split(":")
        draws = split_by_semicolon[1].strip().split(";")
        games = {}
        for draw in draws:
            # convert draw string to dict
            split_by_game = draw.split(",")
            for game in split_by_game:
                split_by_space = game.split()
                # check if the cube color exists and if it's smaller than the current one, if so update it
                if games.get(split_by_space[1]) is not None:
                    if int(split_by_space[0]) > games[split_by_space[1]]:
                        games[split_by_space[1]] = int(split_by_space[0])
                else:
                    games[split_by_space[1]] = int(split_by_space[0])
        power_of_minimum_cubes = 1
        for key in games:
            power_of_minimum_cubes *= games[key]
        result += power_of_minimum_cubes
    return result

file = open("input.txt").readlines()
print("Sum of IDs of possible games: ", part_one())
print("Sum of powers of the minimum sets of cubes in games: ", part_two())