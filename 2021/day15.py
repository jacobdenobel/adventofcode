from queue import PriorityQueue

def dijkstra(grid, growth=1):
    distance = {(0, 0): 0}
    previous = dict()
    n, m = len(grid) * growth, len(grid[0]) * growth
    nn, mm = len(grid), len(grid[0])

    Q = PriorityQueue()
    
    for i in range(n):
        for j in range(m):
            if sum((i,j)) != 0:
                distance[(i,j)] = float("inf")
                previous[(i,j)] = None
    
    Q.put((0, (0, 0)))

    while not Q.empty():
        min_dist, node = Q.get()
        if node != (n - 1, m - 1):
            for d in ((0, 1), (1, 0)):
                new_node = node[0]+d[0], node[1] + d[1]
                if new_node[0] >= n or new_node[1] >= m:
                    continue
                
                g = (new_node[0] // nn) + (new_node[1] // mm)
                dist = ((grid[new_node[0] % nn][new_node[1] % mm] + g) % 9) or 9
                if new_node[0] == 100: breakpoint()
                
                alt = min_dist + dist
                if alt < distance[new_node]:
                    distance[new_node] = alt
                    previous[new_node] = node
                    Q.put((alt, new_node))

    return distance, previous     

def max_dist(fname, growth=1):
    with open(fname) as f:
        data = [list(map(int, line.strip())) for line in f]

    n = (len(data) * growth) - 1
    d, p = dijkstra(data, growth)
    return d[(n, n)]

assert max_dist("data/day15.test.txt", 1) == 40
assert max_dist("data/day15.test.txt", 5) == 315

print("Q1:", max_dist("data/day15.txt", 1))
print("Q2:", max_dist("data/day15.txt", 5))



