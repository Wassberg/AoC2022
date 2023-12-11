# with open('Day3/testInput.txt', 'r') as file:
with open('Day3/input.txt', 'r') as file:
    lines = file.read().splitlines()

letter_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
priority_list = list(range(1,53))
priority_sum = 0

for line in lines:
    c1 = slice(0, len(line)//2)
    c2 = slice(len(line)//2, len(line))
    common = ''.join(set(line[c1]).intersection(line[c2]))
    priority_sum += priority_list[letter_list.index(common)]

print(priority_sum)