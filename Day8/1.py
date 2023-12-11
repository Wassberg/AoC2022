#with open('Day8/testInput.txt', 'r') as file:
with open('Day8/input.txt', 'r') as file:
    lines = file.read().splitlines()

tree_grid = []
trees = 0

for line in lines:
    tree_grid.append(list(line))

for x, tree_line in enumerate(tree_grid):
    if x == 0 or x == len(tree_grid)-1:
            trees += len(tree_line)
    else:
        for y, tree in enumerate(tree_line):
            if y == 0 or y == len(tree_line)-1:
                trees += 1
            else:
                blocked = False
                for l_tree in tree_line[0:y]:
                    if tree <= l_tree:
                        blocked = True
                        break
                if blocked == False: 
                    trees += 1
                    continue

                blocked = False
                for r_tree in tree_line[y+1:len(tree_line)]:
                    if tree <= r_tree:
                        blocked = True
                        break
                if blocked == False:
                    trees += 1
                    continue

                blocked = False
                for u_tree in tree_grid[0:x]:
                    if tree <= u_tree[y]:
                        blocked = True
                        break
                if blocked == False:
                    trees += 1
                    continue

                blocked = False
                for d_tree in tree_grid[x+1:len(tree_grid)]:
                    if tree <= d_tree[y]:
                        blocked = True
                        break
                if blocked == False:
                    trees += 1
                    continue
                
print(trees)