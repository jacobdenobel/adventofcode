with open('data/day11.txt') as f:
    data = [list(map(int, line.strip())) for line in f]


def try_remove(lst, v):
    try:
        lst.remove(v)
    except ValueError:
        pass


def get_surrounding_points(i, j, n=10, m=10):
    all_surrounding_points = [
       (0, 1), (1, 0), (0, -1), (-1, 0),
       (-1, -1), (1, 1), (-1, 1), (1, -1)

    ]
    surrounding_points = all_surrounding_points.copy()
    if i == 0:
        try_remove(surrounding_points, (-1, 0))
        try_remove(surrounding_points, (-1, -1)) 
        try_remove(surrounding_points, (-1, 1))
    if j == 0:
        try_remove(surrounding_points, (0, -1))
        try_remove(surrounding_points, (-1, -1))
        try_remove(surrounding_points, (1, -1))
    if i == (n - 1):
        try_remove(surrounding_points, (1, 0))
        try_remove(surrounding_points, (1, 1))
        try_remove(surrounding_points, (1, -1))
    if j == (m - 1):
        try_remove(surrounding_points, (0, 1))
        try_remove(surrounding_points, (1, 1))
        try_remove(surrounding_points, (-1, 1))

    return [(i+p[0], j + p[1]) for p in surrounding_points]

 
def iter_pos(data):
    for i in range(len(data)):
        for j in range(len(data[0])):
            yield i, j

def get_point(p):
    for i, j in p:
        print(i,j, data[i][j])


def iter_state(data):
    while True:
        stack = list(iter_pos(data))
        has_fired = set()
        while any(stack):
            i, j = stack.pop()
            if not (i,j) in has_fired:
                data[i][j] += 1
            if data[i][j] == 10:
                stack.extend(get_surrounding_points(i, j, len(data), len(data[0])))
                data[i][j] = 0
                has_fired.add((i,j))
        yield len(has_fired)


ii = iter_state(data)
total_fires = 0
for t in range(1000):
    n_fires = next(ii)
    total_fires += n_fires
    if t == 100:
        print("Q1:", total_fires)
    
    if n_fires == len(data) * len(data[0]):
        print("Q2:", t + 1)
        break


   

