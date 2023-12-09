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
    locations = []
    src = int(seed)
    for entity_counter, entity in enumerate(almanac): # loop through types (e.g. seed2soil, etc)
        if entity_counter == 0 : continue
        for item in entity: # loop through each range in type (e.g. each sub-array of seed2soil)
            dest_start = int(item[0])
            src_start = int(item[1])
            range_length = int(item[2])
            src_end = src_start + range_length
            if src_start <= src < src_end :
                src = dest_start + (src - src_start)
                break
        if entity_counter == len(almanac) - 1:
            locations.append(src)
    return min(locations)


def part_one(seeds):
    min_locations = []
    for seed in seeds:
        min_locations.append(min_location_for_seed(seed))
    return min(min_locations)

def part_two():
    seeds_ranges = almanac[0]
    total_min = -1
    for i in range(0, len(seeds_ranges), 2):
        range_start = int(seeds_ranges[i])
        range_end = range_start + int(seeds_ranges[i+1]) # not inclusive
        print('seeds range start = ', range_start)
        print('seeds range end = ', range_end)
        for j in range(range_start, range_end):
            min_location = min_location_for_seed(j)
            if total_min < 0 or min_location < total_min:
                total_min = min_location
    return total_min


initialize_almanac()
print('Single seeds location: ', part_one(almanac[0]))

start_time = time.time()
print('Single seeds location using ranges: ', part_two())
print("Time to run: ", time.time() - start_time)