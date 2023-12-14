import os

def list_files(startpath):
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        print('{}{}/'.format(indent, os.path.basename(root)))
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            print('{}{}'.format(subindent, f))

day = input("Day number to prep for: ")

while not day.isdigit():
    print("Only digits allowed, try again.")
    day = input("Day number to prep for: ")

if len(day) == 1:
    day = "0" + day

# Create directory
# TODO get puzzle's name from adventofcode.com and use it as part of path name
path = "./day" + day
os.mkdir(path) 

# Creates files
filepath = os.path.join(path, 'day' + day + '.py')
with open(filepath, 'w') as fp:
    pass
filepath = os.path.join(path, 'input.txt')
with open(filepath, 'w') as fp:
    # TODO retrieve daily input and save it to file
    pass

print("Directory and files created:")
list_files(path)