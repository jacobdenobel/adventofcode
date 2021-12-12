from collections import defaultdict, Counter
forward = defaultdict(list)
backward = defaultdict(list)

with open("data/day12.txt") as f:
    for line in f:
        src, tgt = line.strip().split("-")
        forward[src].append(tgt)
        backward[tgt].append(src)


def get_all_paths(forward, backward, q1 = True):
    stack = [['start', x] for x in set(forward['start'] + backward['start'])]
    paths = []
    while any(stack):
        *path, node = stack.pop()
        if node == 'end':
            paths.append(tuple(path + [node]))
            continue
        nodes = set(forward[node] + backward[node])
        if q1:
            nodes -= set(x for x in path if x.islower())
        else:
            c = Counter(path + [node])
            has_two = [k for k, v in c.items() if k.islower() and v == 2]
            t = ['start']
            if any(has_two):
                for k, v in c.items():
                    if k.islower():
                        t.append(k)
                
            nodes -= set(t)
            
        if any(nodes):
            for n in nodes:
                stack.append(path + [node, n])
    return set(paths)

print("Q1:", len(get_all_paths(forward, backward)))
print("Q2:", len(get_all_paths(forward, backward, False)))

    
