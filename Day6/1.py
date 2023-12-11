#with open('Day6/testInput.txt', 'r') as file:
with open('Day6/input.txt', 'r') as file:
    lines = file.read().splitlines()

buffer = lines[0]
WINDOW_SIZE = 4
w_start = 0
w_end = WINDOW_SIZE
window = set()

while(w_end < len(buffer)):
    window = set()
    for char in buffer[w_start:w_end]:
        window.add(char)
    if(len(window) == WINDOW_SIZE):
        break
    w_start += 1
    w_end += 1

print(w_end)