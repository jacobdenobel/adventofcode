from collections import namedtuple
from itertools import chain 

Point = namedtuple("Point", ["x", "y"])

def display(grid):
    for g in grid:
        print(''.join(map(lambda x:str(x) if x else '.', g)))

def make_line(source, target, diagonals=True):
    if diagonals:
        deltax = target.x - source.x
        deltay = target.y - source.y 
        sx = 1 if deltax > 0 else -1
        sy = 1 if deltay > 0 else -1
        if abs(deltay) == abs(deltax) and deltax:
            for dx in range(abs(deltax) + 1):
                yield Point(source.x + (dx * sx), source.y + (dx * sy))

    if not (source.x == target.x or source.y == target.y): return
    def inner(source, target):
        for x in range(source.x, target.x + 1):
            for y in range(source.y, target.y + 1):
                yield Point(x, y)

    yield from inner(source, target)
    yield from inner(target, source)

def compute_crossings(maxx, maxy, points):
    grid = [[0] * (maxy + 1) for x in range(maxx + 1)]
    for point in points:
        grid[point.y][point.x] += 1

    s = 0
    for row in grid:
        for p in row:
            if p > 1:
                s += 1
    return s

if __name__ == '__main__':
    points = []
    maxy, maxx = 0, 0
    with open("data/day5.txt") as f:
        for line in f:
            source, target = map(
                    lambda s: Point(*map(int, s.split(","))), 
                    line.strip().split(" -> ")
            )
            maxx = max(maxx, source.x, target.x)
            maxy = max(maxy, source.y, target.y)
            points.append((source, target))



    print("Q1:", compute_crossings(maxx, maxy, chain.from_iterable(map(lambda p: make_line(*p, False), points))))
    print("Q2:", compute_crossings(maxx, maxy, chain.from_iterable(map(lambda p: make_line(*p, True), points)))
            )
