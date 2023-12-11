#with open('Day2/testInput.txt', 'r') as file:
with open('Day2/input.txt', 'r') as file:
    lines = file.read().splitlines()

score_dict = {
    "A": 1,
    "B": 2,
    "C": 3,
}
win_dict = {
    "A": "B",
    "B": "C",
    "C": "A"
}
fail_dict = {
    "A": "C",
    "B": "A",
    "C": "B"
}

score = 0
for line in lines:
    if(line[2] == 'X'):
        score += score_dict[fail_dict[line[0]]]
    elif(line[2] == 'Y'):
        score += score_dict[line[0]] + 3
    else:
        score += score_dict[win_dict[line[0]]] + 6

print(score)