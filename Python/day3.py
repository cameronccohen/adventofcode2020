# Part 1

with open('../Input/day3_input.txt') as f:
    grid = f.read().splitlines()

col_width = len(grid[0])
def traverse(i,j, y, x):
    return i+y, (j+x) % col_width

i, j = 0,0
trees = 0
while i < len(grid):
    trees += (grid[i][j] == '#')
    i,j = traverse(i, j, 1, 3)

print(trees)

# # Part 2
import math

slopes = [(1,1), (1, 3), (1, 5), (1, 7), (2, 1)]
trees = [0]*len(slopes)
for i, slope in enumerate(slopes):
    x, y = 0,0
    while y < len(grid):
        trees[i] += (grid[y][x] == '#')
        y,x = traverse(y, x, *slope)

print(math.prod(trees))

