def parse_file():
    time, distance, ways_to_win = [], [], []
    with open("input.txt") as input_file:
        for i, line in enumerate(input_file.readlines()):
            temp = line.split(':')
            if i == 0:
                for item in temp[1].strip().split():
                    time.append(int(item))
            elif i == 1:
                for item in temp[1].strip().split():
                    distance.append(int(item))
        i = 0
        while i < len(time):
            ways_to_win.append(0)
            i += 1
    return time, distance, ways_to_win

def fix_kerning(input):
    temp = ''
    for item in input:
        temp += str(item)
    return [int(temp)]

def part_one(time, distance, ways_to_win):
    for race_index, race_duration in enumerate(time):
        hold_for = 0
        record_distance_for_race = distance[race_index]
        while hold_for < race_duration:
            hold_for += 1
            distance_travelled = hold_for * (race_duration - hold_for)
            if distance_travelled > record_distance_for_race:
                ways_to_win[race_index] += 1
    result = ways_to_win[0]
    for i in range(1, len(ways_to_win)):
        result = result * ways_to_win[i]
    return result

def part_two(time, distance):
    return part_one(fix_kerning(time), fix_kerning(distance), [0])

time, distance, ways_to_win = parse_file()
print('Number of ways I could beat the record in each race (part I): ', part_one(time, distance, ways_to_win))
print('Number of ways I could beat the record in each race (part II): ', part_two(time, distance))