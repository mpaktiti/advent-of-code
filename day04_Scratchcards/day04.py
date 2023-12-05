import sys; sys.path.insert(0, "../utils")
import utils

def build_array_from_file():
    cards = []
    for line in utils.read_input():
        cards.append(line.strip())
    return cards

# part 1: add up the part numbers
def part_one():
    # read file and copy characters to array
    cards = build_array_from_file()
    result = 0
    for card in cards:
        points = 0
        split_info = card.split("|")
        left_part = split_info[0].split(":")
        winning_numbers = left_part[1].split()
        own_numbers = split_info[1].split()
        winning_cards = 0
        for number in own_numbers:
            if number in winning_numbers:
                winning_cards += 1
        if winning_cards == 1 or winning_cards == 2:
            points = winning_cards
        elif winning_cards > 2:
            points = 2**(winning_cards-1)
        result += points
    return result

print("Total cards worth: ", part_one())