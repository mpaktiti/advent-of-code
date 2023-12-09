def copy_file_to_array():
    file = open('input.txt').readlines()
    cards = [line.strip() for line in file]
    return cards

def num_of_matching_numbers(card):
    split_info = card.split("|")
    left_part = split_info[0].split(":")
    winning_numbers = left_part[1].split()
    own_numbers = split_info[1].split()
    winning_cards = len([i for i in own_numbers if i in winning_numbers ])
    return winning_cards

# part 1: add up the part numbers
def part_one():
    # read file and copy characters to array
    cards = copy_file_to_array()
    result = 0
    for card in cards:
        points = 0
        winning_cards = num_of_matching_numbers(card)
        if winning_cards == 1 or winning_cards == 2:
            points = winning_cards
        elif winning_cards > 2:
            points = 2**(winning_cards-1)
        result += points
    return result

def find_next_item_to_insert(pos, cards):
    item_to_insert = pos + 1
    insert_position = pos + 2
    item_found = False
    while not item_found:
        if cards[item_to_insert][:4] == "COPY":
            item_to_insert += 1
            insert_position += 1
            continue
        item_found = True
    return item_to_insert, insert_position

def part_two():
    cards = copy_file_to_array()

    # SECOND APPROACH
    cards_copies = {}
    for pos, item in enumerate(cards, 1):
        cards_copies[pos] = 1

    for pos in range(0, len(cards)):
        num_of_iterations = cards_copies[pos+1]
        counter = num_of_matching_numbers(cards[pos])
        if counter > 0:
            start = pos + 1
            end = start + counter
            while start < end:
                cards_copies[start+1] += num_of_iterations
                start += 1
    return sum(cards_copies.values())


print("Total cards worth: ", part_one())
print("Total number of cards: ", part_two())