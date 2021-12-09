import functools
import operator


with open("data/day9.txt") as f:
    data = []
    for line in f:
        data.append(list(map(int, line.strip())))

def get_surrounding_points(i, j, n, m):
    all_surrounding_points = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    surrounding_points = all_surrounding_points.copy()
    if i == 0:
        surrounding_points.remove((-1, 0))
    if j == 0:
        surrounding_points.remove((0, -1))
    if i == (n - 1):
        surrounding_points.remove((1, 0))
    if j == (m - 1):
        surrounding_points.remove((0, 1))
    return [(i+p[0], j + p[1]) for p in surrounding_points]

def get_low_points(data):
    n = len(data)
    m = len(data[0])
    for i, row in enumerate(data):
        for j, col in enumerate(row):
            surrounding_points = get_surrounding_points(i, j, n, m)
            value = data[i][j] 
            if all(data[p[0]][p[1]] > value for p in surrounding_points):
                yield i, j, value 

def get_basin(i, j, value, data):
    n = len(data)
    m = len(data[0])

    stack = [(i,j)] 
    seen  = set()
    while any(stack):
        point = stack.pop(0)
        h = data[point[0]][point[1]]

        seen.add(point)
        for ii, jj in get_surrounding_points(*point, n, m):
            hp = data[ii][jj]

            if (ii, jj) not in seen and hp > h and hp != 9:
                stack.append((ii, jj))
    return len(seen)


if __name__ == '__main__':
    print("Q1:", sum(map(lambda x:x[2] + 1, get_low_points(data))))
    basins = []
    for i, j, value in get_low_points(data):
        basins.append(get_basin(i, j, value, data))

    print("Q2:", functools.reduce(operator.mul, sorted(basins, reverse=True)[:3], 1))
