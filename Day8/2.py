#with open('Day8/testInput.txt', 'r') as file:
with open('Day8/input.txt', 'r') as file:
    lines = file.read().splitlines()

tree_grid = []
scenic_scores = []

for line in lines:
    tree_grid.append(list(line))

for x, tree_line in enumerate(tree_grid):
    if x == 0 or x == len(tree_grid)-1:
            continue
    else:
        for y, tree in enumerate(tree_line):
            if y == 0 or y == len(tree_line)-1:
                continue
            else:
                blocked = False
                l_trees = 0
                for l_tree in tree_line[y-1::-1]:
                    l_trees += 1
                    if tree <= l_tree:
                        break
                
                r_trees = 0        
                for r_tree in tree_line[y+1:len(tree_line)]:
                    r_trees += 1
                    if tree <= r_tree:
                        break

                u_trees = 0
                for u_tree in tree_grid[x-1::-1]:
                    u_trees += 1
                    if tree <= u_tree[y]:
                        break


                d_trees = 0
                for d_tree in tree_grid[x+1:len(tree_grid)]:
                    d_trees += 1
                    if tree <= d_tree[y]:
                        break
                scenic_scores.append(l_trees*r_trees*u_trees*d_trees)

            
                
print(max(scenic_scores))