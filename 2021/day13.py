from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])

data = []
folds = []
X, Y = 0,0
with open("data/day13.txt") as f:
    for line in f:
        if line[0].isdigit():
            p = Point(*map(int, line.strip().split(",")))
            data.append(p)
            X = max(X, p.x)
            Y = max(Y, p.y)
        elif line.startswith("fold"):
            *_, fold = line.strip().split()
            along, coord = fold.split("=")
            folds.append((along, int(coord)))

grid = [[(x, y) in data for x in range(X+1)] for y in range(Y+1)]

def display(grid):
    for x in grid[::-1]:
        print(''.join(map(lambda x: "#" if x else ".", x[::-1])))

def fold_grid(grid, fold):
    along, coord = fold
    if along == "y":
        bottom = grid[:coord][::-1]
        top = grid[coord+1:]
    else:
        bottom = [x[:coord][::-1] for x in grid]
        top = [x[coord+1:] for x in grid]
    for i, x in enumerate(top):
        for j, (y1, y2) in enumerate(zip(x, bottom[i])):
            bottom[i][j] = y1 or y2
    return bottom

def iter_folds(grid, folds):
    for fold in folds:
        grid = fold_grid(grid, fold)
        yield grid

ii = iter_folds(grid, folds)

print("Q1:",  sum(sum(x) for x in next(ii)))
for i in ii:
    pass
display(i)



