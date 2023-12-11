#with open('Day2/testInput.txt', 'r') as file:
with open('Day2/input.txt', 'r') as file:
    lines = file.read().splitlines()

score_dict = {
    "A": 1,
    "B": 2,
    "C": 3,
    "X": 1,
    "Y": 2,
    "Z": 3
}
beat_dict = {
    "A": "Z",
    "B": "X",
    "C": "Y"
}

score = 0
for line in lines:
    score += score_dict[line[2]]
    if(score_dict[line[0]] == score_dict[line[2]]):
        score += 3
    elif(beat_dict[line[0]] != line[2]):
        score += 6

print(score)