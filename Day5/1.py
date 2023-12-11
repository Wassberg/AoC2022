#with open('Day5/testInput.txt', 'r') as file:
with open('Day5/input.txt', 'r') as file:
    lines = file.read().splitlines()

stack_count_line = 0
movement_lines = 0

for x, line in enumerate(lines):
    if not any(y in line for y in ["[", "move"]) and not len(line) == 0:
        stack_count_line = x
    elif 'move' in line:
        movement_lines = x
        break
    
stacks = [[] for x in range(0,len(lines[stack_count_line].strip().split()))]
for line in lines[0 : stack_count_line]:
    container_row = list(line.replace('    ', '[0]').replace(' ', '').replace('[', '').replace(']', ''))
    for x, container in enumerate(container_row):
        if(container != '0'):
            stacks[x].append(container)

for stack in stacks:
    stack.reverse()

for line in lines[movement_lines: len(lines)]:
    count, dest_stack, target_stack = [int(s) for s in line.split() if s.isdigit()]
    for i in range(count):
        if(len(stacks[dest_stack-1]) > 0):
            container = stacks[dest_stack-1].pop()
            stacks[target_stack-1].append(container)

result = ""
for stack in stacks:
    if(len(stack) > 0):
        result += stack.pop()

print(result)    