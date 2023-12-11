# with open('Day1/testInput.txt', 'r') as file:
with open('Day1/input.txt', 'r') as file:
    lines = file.read().splitlines()

elves = []
elf_cals = 0
for line in lines:
    if line == '':
        elves.append(elf_cals)
        elf_cals = 0
    else:
        elf_cals += int(line)
elves.append(elf_cals)
elves.sort(reverse=True)
print(sum(elves[0:3]))