import sys; sys.path.insert(0, '../utils')
import utils

def create_seed_entry(item):
    seed = {}
    seed['seed'] = item
    seed['soil'] = '-'
    seed['fertilizer'] = '-'
    seed['water'] = '-'
    seed['light'] = '-'
    seed['temperature'] = '-'
    seed['humidity'] = '-'
    seed['location'] = '-'
    return seed

def initialize_maps():
    seeds = []
    almanac_maps = {}
    code = ''
    for line in utils.read_input():
        if line.isspace():
            continue
        if line[:6] == 'seeds:':
            temp = line.split(':')
            seed_numbers = temp[1].split()
            for item in seed_numbers:
                seeds.append(create_seed_entry(item))
        elif line[:1].isdigit():
            temp = line.strip().split()
            almanac_maps[code].append(temp)
        else:
            temp = line.split()
            almanac_maps[temp[0]] = []
            code = temp[0]
    return seeds, almanac_maps

def map_source_to_destination(map, seed_num):
    for item in map:
        dest_start = int(item[0])
        src_start = int(item[1])
        len = int(item[2])
        src_end = src_start + len # not inclusive
        if seed_num >= src_start and seed_num < src_end:
            dest = dest_start + (seed_num - src_start)
            res = dest
            break
        else:
            res = seed_num
    return res

# part 1: find the nearest location
def part_one():
    seeds, almanac_maps = initialize_maps()
    # loop through seeds
    # for each seed search all maps one by one
    min_location = 0
    for seed in seeds:
        seed_num = int(seed['seed'])
        seed['soil'] = map_source_to_destination(almanac_maps['seed-to-soil'], seed_num)
        seed['fertilizer'] = map_source_to_destination(almanac_maps['soil-to-fertilizer'], seed['soil'])
        seed['water'] = map_source_to_destination(almanac_maps['fertilizer-to-water'], seed['fertilizer'])
        seed['light'] = map_source_to_destination(almanac_maps['water-to-light'], seed['water'])
        seed['temperature'] = map_source_to_destination(almanac_maps['light-to-temperature'], seed['light'])
        seed['humidity'] = map_source_to_destination(almanac_maps['temperature-to-humidity'], seed['temperature'])
        seed['location'] = map_source_to_destination(almanac_maps['humidity-to-location'], seed['humidity'])
        if min_location == 0:
            min_location = seed['location']
        elif seed['location'] < min_location:
            min_location = seed['location']
    return min_location

print('Start planting at location: ', part_one())