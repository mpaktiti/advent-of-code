import functools

cards = {}
types = {'FIVE': 7, 'FOUR': 6, 'FULL_HOUSE': 5, 'THREE': 4, 'TWO': 3, 'ONE': 2, 'HIGH': 1}
weights = {'A': 5, 'K': 4, 'Q': 3, 'J': 2, 'T': 1}

# open file and return contents to caller
def read_input():
    with open("input.txt") as input_file:
        return input_file.readlines()

# read cards from file and copy them to memory
def read_cards():
    for line in read_input():
        temp = line.strip().split()
        cards[temp[0]] = {'bid': int(temp[1])}
    print('Cards read from file: ', cards)

# helper function that checks if the characters of card, excluding same_char, make a pair or are different
def remaining_chars_make_pair(card, same_char):
    remaining_chars=card.replace(same_char,"")
    if len(remaining_chars) == 2:
        return remaining_chars[0] == remaining_chars[1]
    else: # remaining_chars is 3
        for char in remaining_chars:
            if card.count(char) == 2:
                return True
        return False

# checks if the input is a five of a kind, where all five cards have the same label: AAAAA
def is_five(card):
    return card.count(card[0]) == 5

# checks if the input is a four of a kind, where four cards have the same label and one card has a different label: AA8AA
def is_four(card):
    for char in card:
        if card.count(char) == 4:
            return True
    return False

# checks if the input is a full house, where three cards have the same label, and the remaining two cards 
# share a different label: 23332
def is_full_house(card):
    for char in card:
        if card.count(char) == 3:
            return remaining_chars_make_pair(card, char)
    return False

# checks if the input is a three of a kind, where three cards have the same label, and the remaining two cards 
# are each different from any other card in the hand: TTT98
def is_three(card):
    for char in card:
        if card.count(char) == 3:
            return not remaining_chars_make_pair(card, char)
    return False

# checks if the input is a two pair, where two cards share one label, two other cards share a second label, 
# and the remaining card has a third label: 23432
def is_two(card):
    for char in card:
        if card.count(char) == 2:
            return remaining_chars_make_pair(card, char)
    return False

# checks if the input is a one pair, where two cards share one label, and the other three cards have a different label 
# from the pair and each other: A23A4
def is_one(card):
    for char in card:
        if card.count(char) == 2:
            return not remaining_chars_make_pair(card, char)
    return False

# for each card find its type and set it as part of the dictionary
def calculate_type():
    for card in cards:
        print(card)
        if is_five(card):
            cards[card]['type'] = 'FIVE'
        elif is_four(card):
            cards[card]['type'] = 'FOUR'
        elif is_full_house(card):
            cards[card]['type'] = 'FULL_HOUSE'
        elif is_three(card):
            cards[card]['type'] = 'THREE'
        elif is_two(card):
            cards[card]['type'] = 'TWO'
        elif is_one(card):
            cards[card]['type'] = 'ONE'
        else:
            cards[card]['type'] = 'HIGH'
    print('Cards with type: ', cards)

def weight_chars(x, y):
    if weights[x] < weights[y]:
        return -1
    elif weights[x] > weights[y]:
        return 1
    else:
        return 0

def compare(x, y):
    # 1st level ranking
    x_type_rank = types[cards[x]['type']]
    y_type_rank = types[cards[y]['type']]
    if x_type_rank < y_type_rank:
        return -1
    elif x_type_rank > y_type_rank:
        return 1
    
    # if still here than we proceed to 2nd level ranking
    i = -1
    for char in x:
        i += 1
        if char == y[i]:
            continue
        elif char.isalpha(): 
            if y[i].isdigit():
                return 1
            return weight_chars(char, y[i])
        elif char.isdigit():
            if y[i].isalpha():
                return -1
            # both chars are digits
            if int(char) < int(y[i]):
                return -1
            elif int(char) > int(y[i]):
                return 1
            else:
                return 0

def calculate_strength():
    # first ranking: type
    # if the type is the same then we do the 2nd level ranking
    sorted_cards = sorted(cards, key=functools.cmp_to_key(compare), reverse=True)
    print(sorted_cards)
    current_rank = len(sorted_cards)
    for item in sorted_cards:
        cards[item]['rank'] = current_rank
        current_rank -= 1
    print(cards)

def total_winnings():
    total = 0
    for card in cards:
        print('card: ', cards[card])
        print('bid: ', cards[card]['bid'])
        print('rank: ', cards[card]['rank'])
        total += cards[card]['bid'] * cards[card]['rank']
        print('total = ', total)
    return total

read_cards()
calculate_type()
calculate_strength()
print('Total winnings: ', total_winnings())

