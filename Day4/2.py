#with open('Day4/testInput.txt', 'r') as file:
with open('Day4/input.txt', 'r') as file:
    lines = file.read().splitlines()

result = 0
for line in lines:
    range1 = line.split(',')[0].split('-')
    range2 = line.split(',')[1].split('-')
    elf1 = list(range(int(range1[0]), int(range1[1])+1))
    elf2 = list(range(int(range2[0]), int(range2[1])+1))
    if any(elem in elf1 for elem in elf2):
        result += 1

print(result)