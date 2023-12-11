with open('Day9/testInput.txt', 'r') as file:
#with open('Day9/input.txt', 'r') as file:
    lines = file.read().splitlines()

ROPE_LENGTH = 10
node_list = []
for i in range(ROPE_LENGTH):
    node_list.append({'x':0, 'y':0})
t_pos = set()

def move_node(node_list, i, d):
    if i == 0:
        if d == 'L': move_left(node_list[i])
        if d == 'R': move_right(node_list[i])
        if d == 'U': move_up(node_list[i])
        if d == 'D': move_down(node_list[i])
    else:
        x_move = y_move = 0
        snap_x = snap_y = False
        if node_list[i]['x'] - node_list[i-1]['x'] > 1:
            x_move -= 1
            snap_y = True
        if node_list[i]['x'] - node_list[i-1]['x'] < -1:
            x_move += 1
            snap_y = True
        if node_list[i]['y'] - node_list[i-1]['y'] < -1:
            y_move += 1
            snap_x = True
        if node_list[i]['y'] - node_list[i-1]['y'] > 1:
            y_move -= 1
            snap_x = True
        node_list[i]['x'] += x_move
        node_list[i]['y'] += y_move
        if snap_x and not snap_y: node_list[i]['x'] = node_list[i-1]['x']
        if snap_y and not snap_x: node_list[i]['y'] = node_list[i-1]['y']

def move_left(node):
    node['x'] -= 1

def move_right(node):
    node['x'] += 1
    
def move_up(node):
    node['y'] += 1

def move_down(node):
    node['y'] -= 1

for line in lines:
    d = line.split(' ')[0]
    l = int(line.split(' ')[1])
    for a in range(l):
        for i, node in enumerate(node_list):
            move_node(node_list, i, d)
        t_pos.add(str(node_list[ROPE_LENGTH-1]['x'])+','+str(node_list[ROPE_LENGTH-1]['y']))

print(len(t_pos))