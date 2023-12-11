#with open('Day7/testInput.txt', 'r') as file:
with open('Day7/input.txt', 'r') as file:
    lines = file.read().splitlines()

dirs = {}
current_dir = []
abs_path = ''
MAX_SPACE = 70000000
REQ_SPACE = 30000000

for line in lines:
    if 'cd ' in line:
        dir = line.split('cd ')[1]
        if(dir == '..' and len(current_dir) > 0):
            current_dir.pop()
        else:
            current_dir.append(dir + '|')
        abs_path = ''.join(current_dir)
        if not abs_path in dirs:
            dirs.update({abs_path: 0})
    if line.split(' ')[0].isdigit():
        b_dir = current_dir.copy()
        while(len(b_dir)>0):
            dirs[''.join(b_dir)] += int(line.split(' ')[0])
            b_dir.pop()

unused_space = MAX_SPACE - dirs['/|']
needed_space = REQ_SPACE - unused_space
dir_sizes = []
for dir in dirs:
    if dirs[dir] > needed_space:
        dir_sizes.append(dirs[dir])


print(min(dir_sizes))