#with open('Day9/testInput.txt', 'r') as file:
with open('Day9/input.txt', 'r') as file:
    lines = file.read().splitlines()

h = {'x':0, 'y':0}
t = {'x':0, 'y':0}
t_pos = set()

for line in lines:
    d, l = line.split(' ')
    l = int(l)

    if d == 'L':
        for a in range(l):
            if t['x'] > h['x']:
                t['x'] -= 1
                t['y'] = h['y']
            h['x'] -= 1
            t_pos.add(str(t['x']) + ',' + str(t['y']))

    elif d == 'R':
       for a in range(l):
            if t['x'] < h['x']:
                t['x'] += 1
                t['y'] = h['y']
            h['x'] += 1
            t_pos.add(str(t['x']) + ',' + str(t['y']))

    elif d == 'U':
       for a in range(l):
            if t['y'] < h['y']:
                t['y'] += 1
                t['x'] = h['x']
            h['y'] += 1
            t_pos.add(str(t['x']) + ',' + str(t['y']))

    elif d == 'D':
       for a in range(l):
            if t['y'] > h['y']:
                t['y'] -= 1
                t['x'] = h['x']
            h['y'] -= 1
            t_pos.add(str(t['x']) + ',' + str(t['y']))

print(len(t_pos))
