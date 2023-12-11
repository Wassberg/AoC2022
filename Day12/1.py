with open('Day12/testInput.txt', 'r') as file:
# with open('Day12/input.txt', 'r') as file:
    lines = file.read().splitlines()

#Right answer 1 - 330
#Right answer 2 - 321
start = ord('S')
end = ord('E')
start_pos = end_pos = None
mountain_map = []

paths = []

def step_next(current_pos, mountain_map):
    possible_steps = []
    pos_x = current_pos['x']
    pos_y = current_pos['y']
    if (pos_x > 0 and
        mountain_map[pos_x-1][pos_y]['visited'] == True):
        return


for i, line in enumerate(lines):
    mountain_map.append([{'value' :ord(n), 'visited': False} for n in line])
    for j, c in enumerate(line):
        if ord(c) == start:
            start_pos = {'x' : j, 'y' : i}
        if ord(c) == end:
            end_pos = {'x' : j, 'y' : i}
        
find_paths = True
current_position = start_pos

print(start_pos)
