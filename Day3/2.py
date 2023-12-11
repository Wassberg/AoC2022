#with open('Day3/testInput.txt', 'r') as file:
with open('Day3/input.txt', 'r') as file:
    lines = file.read().splitlines()

letter_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
priority_list = list(range(1,53))
priority_sum = 0
GROUP_SIZE = 3

line_index = 0
while(line_index < len(lines)):
    elf1 = lines[line_index]
    elf2 = lines[line_index+1]
    elf3 = lines[line_index+2]
    common = ''.join(set(elf1).intersection(elf2).intersection(elf3))
    priority_sum += priority_list[letter_list.index(common)]
    line_index += GROUP_SIZE

print(priority_sum)