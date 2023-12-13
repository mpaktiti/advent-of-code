from itertools import combinations
from bisect import bisect

galaxy = []
def read_galaxy():
    file = open('input.txt').readlines()
    for line in file:
        galaxy.append([char for char in line.strip()])

def print_galaxy():
    for i in range(0, len(galaxy)):
        cols = ''
        for col in galaxy[i]:
            cols += col
        print(cols)

def column(matrix, i):
    return [row[i] for row in matrix]

def expand_galaxy():
    lines = []
    for i, item in enumerate(galaxy):
        if item.count('.') == len(item):
            lines.append(i)
    # lines = [i for i, item in enumerate(galaxy) if item.count('.') == len(item)]
    print('lines to repeat: ', lines)
    
    cols = []
    for i in range(len(galaxy[0])):
        if column(galaxy, i).count('.') == len(galaxy[i]):
            cols.append(i)
    print('columns to repeat: ', cols)

    # add lines
    for i, item in enumerate(lines):
        galaxy.insert(item+i, ['.'] * len(galaxy[0]))

    # add columns
    for i, col in enumerate(cols):
        for row in galaxy:
            row.insert(col+i,'.')
    return lines, cols

def calculate_lengths():
    # find where the galaxies are located
    galaxies = []
    for y, row in enumerate(galaxy):
        for x, col in enumerate(row):
            if col != ".":
                galaxies.append((x, y))
    print('galaxies: ', galaxies)

    # generate a list of all galaxy combos
    pairs = list(combinations(galaxies, 2))
    print('pairs: ', pairs)

    # use Manhattan distance
    count = 0
    for p1, p2 in pairs:
        count += abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

    return count
# 1. read galaxy image
read_galaxy()
print_galaxy()

# 2. expand galaxy
print('calculating cosmic expansion...')
empty_columns, empty_rows = expand_galaxy()
print_galaxy()

# 3. find the galaxies and sum the distance between pairs
print('sum of shortest path lengths: ', calculate_lengths())

# 4. find the galaxies and sum the distance between pairs expanded by 1 million
# print('sum of shortest path lengths (1 million): ', calculate_lengths())