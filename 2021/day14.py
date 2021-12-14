from collections import Counter
from itertools import chain, tee
from functools import lru_cache

rules = dict() 

with open("data/day14.txt") as f:
    template = next(f).strip()
    next(f)
    for line in f:
        src, tgt = line.strip().split(" -> ")
        rules[tuple(src)] = tgt

@lru_cache
def join_pair(pair):
    return pair[0] + rules[pair]

def simulate(template):
    next_gen = iter(template)
    while True:
        a, b = tee(next_gen)
        next(b, None)
        next_gen = map(join_pair, zip(a, b))
        next_gen = chain(chain.from_iterable(next_gen), iter([template[-1]]))   
        next_gen, a = tee(next_gen) 
        yield a

def experiment(t):
    ii = simulate(template)
    for i in range(t):
        next_gen = next(ii)
    
    counts = Counter(next_gen)
    return max(counts.values()) - min(counts.values())

print("Q1:", experiment(10))
print("Q2:", experiment(40))

