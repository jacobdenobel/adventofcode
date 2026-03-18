from itertools import combinations

def distance(x, y):
    return sum((xi - yi)**2 for xi, yi in zip(x, y))

def pdist(data, skip = None):
    if skip is None:
        skip = []
        
    min_dist = float("inf")
    min_xy = None
    for x, y in combinations(range(len(data)), 2):
        if (x, y) in skip:
            continue
        dist = distance(data[x], data[y])
        if dist < min_dist:
            min_dist = dist
            min_xy = x, y
    return min_xy, min_dist


junctions = []
with open("data/8_test") as f:
    for line in f:
        junctions.append(list(map(int, line.strip().split(","))))


circuits = []
for _ in range(5):
    (x, y), d = pdist(junctions, circuits)
    print(junctions[x], junctions[y])
    circuits.append((x, y))
    
print(circuits)