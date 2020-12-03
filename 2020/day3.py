from pprint import pprint 
from math import prod


with open("data/3.txt", "r") as f:
    grid = [
        line.strip()
        for line in f
    ]

def traverse_and_count_trees(grid, down=1, right=3):
    row, col = 0,0
    n_trees = 0
    height = len(grid)
    width = len(grid[0])
    while row < height: 
        if grid[row][col] == '#': n_trees += 1 
        row += down
        col += right
        if col >= width: col -= width
    
    return n_trees

print("Q1", traverse_and_count_trees(grid))
print("Q2", prod(traverse_and_count_trees(grid, down, right) 
    for down, right in ( (1,1), (1, 3), (1, 5), (1, 7), (2, 1))))


