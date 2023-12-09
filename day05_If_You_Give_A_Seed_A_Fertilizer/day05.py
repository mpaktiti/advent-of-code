import time

almanac = []
# initialize almanac
def initialize_almanac():
    temp_ranges = []
    file = open("input.txt").readlines()
    for line in file:
        if line.isspace():
            if len(temp_ranges) > 0:
                almanac.append(temp_ranges)
                temp_ranges = []
            continue
        elif line[:1].isdigit():
            temp_ranges.append(line.split())
        elif line[:6] == 'seeds:': # first line of file is different
            temp = line.strip().split(':')
            almanac.append(temp[1].split())
    almanac.append(temp_ranges)

def min_location_for_seed(seed):
    entity_counter = 0
    locations = []
    src = int(seed)
    for entity in almanac: # loop through types (e.g. seed2soil, etc)
        if entity_counter == 0:
            entity_counter += 1
            continue
        # print('entity: ', entity)
        for item in entity: # loop through each range in type (e.g. each sub-array of seed2soil)
            # print('range in entity: ', item)
            dest_start = int(item[0])
            src_start = int(item[1])
            range_length = int(item[2])
            src_end = src_start + range_length
            if src_start <= src < src_end :
                # print('src is within range ', src_start, " - ", src_end)
                src = dest_start + (src - src_start)
                break
        # print('match for entity = ', src)
        if entity_counter == len(almanac) - 1:
            # print('min location for seed ', seed, 'is ', src)
            locations.append(src)
        entity_counter += 1
    return min(locations)


def part_one(seeds):
    min_locations = []
    for seed in seeds:
        # print('seed: ', seed)
        min_locations.append(min_location_for_seed(seed))
    return min(min_locations)

def part_two():
    seeds_ranges = almanac[0]
    i = 0
    total_min = -1
    while i < len(seeds_ranges):
        range_start = int(seeds_ranges[i])
        range_end = range_start + int(seeds_ranges[i+1]) # not inclusive
        print('seeds range start = ', range_start)
        print('seeds range end = ', range_end)
        j = range_start
        while j < range_end:
            min_location = min_location_for_seed(j)
            if total_min < 0 or min_location < total_min:
                total_min = min_location
            j += 1
        i += 2
    return total_min


initialize_almanac()
print('Single seeds location: ', part_one(almanac[0]))

start_time = time.time()
print('Single seeds location using ranges: ', part_two())
print("Time to run: ", time.time() - start_time)