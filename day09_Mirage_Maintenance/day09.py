def generate_sequences(item):
    cur_seq = [int(x) for x in item]
    sequences = [cur_seq]
    while not all(x == 0 for x in cur_seq):
        new_seq = []
        i = 0
        for i in range(len(cur_seq)-1):
            new_seq.append(cur_seq[i+1]-cur_seq[i])
        sequences.append(new_seq)
        cur_seq = new_seq
    return sequences

def extrapolate_history(seq):
    index = -1
    num_to_append = 0
    while True:
        seq[index].append(num_to_append)
        if index + len(seq) == 0 : break
        index -=1
        num_to_append = seq[index][-1] + num_to_append
    return seq[0][-1]

file = open('input.txt').readlines()
report = [line.split() for line in file]

next_nums = []
for item in report:
    seq = generate_sequences(item)
    next_nums.append(extrapolate_history(seq))

print('sum of all next extrapolated values: ', sum(next_nums))

previous_nums = []
for item in report:
    seq = generate_sequences(list(reversed(item)))
    previous_nums.append(extrapolate_history(seq))

print('sum of all previous extrapolated values: ', sum(previous_nums))