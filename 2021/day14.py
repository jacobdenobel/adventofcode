from collections import Counter
from itertools import tee

rules = dict() 

def pairwise(ii):
    a, b = tee(ii)
    next(b)
    return zip(a, b)

with open("data/day14.txt") as f:
    template = next(f).strip()
    next(f)
    for line in f:
        src, tgt = line.strip().split(" -> ")
        rules[tuple(src)] = tgt
    
    counts = Counter(template)
    pairs = Counter(pairwise(template))

for i in range(40):
    for pair, value in pairs.copy().items():
        pairs[pair] -= value
        pairs[tuple([pair[0], rules[pair]])] += value
        pairs[tuple([rules[pair], pair[1]])] += value
        counts[rules[pair]] += value
    if i == 9:
        print("Q1:", max(counts.values()) - min(counts.values()))

print("Q2:", max(counts.values()) - min(counts.values()))

