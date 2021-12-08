from collections import Counter


data = []
q1 = 0
with open("data/day8.txt") as f:
    for line in f:
        inp, out = map(tuple, map(str.split, line.strip().split(" | ")))
        for d in out:
            if len(d) in (2, 3, 4, 7):
                q1 += 1
        data.append((inp, out))

print("Q1:", q1)
numbers = {
    'abcefg': 0,
    'cf': 1,
    'acdeg': 2,
    'acdfg': 3,
    'bcdf': 4,
    'abdfg': 5,
    'abdefg': 6, 
    'acf': 7,
    'abcdefg': 8,
    'abcdfg': 9
}
total = 0
for inp, out in data:
    displays = dict.fromkeys("abcdefg")
    lens = list(map(len, inp))
    displays['a'], *_  = set(inp[lens.index(3)]) - set(inp[lens.index(2)])

    one = Counter(inp[lens.index(2)])
    seven = Counter(inp[lens.index(3)])
    four = Counter(inp[lens.index(4)])

    c = Counter(''.join(x for x in inp if len(x) == 6))
    displays['e'], *_ = [k for k,v in (c + four).items() if v == 2]
    displays['f'], *_ = [k for k,v in (c + one).items() if v == 4]
    displays['c'], *_ = set(one.keys()) - {displays['f']}

    c5 = Counter(''.join(x for x in inp if len(x) == 5))

    rem = Counter(''.join(x for x in inp if len(x) > 4))
    displays['d'], *_ = [k for k,v in (c5 + four).items() if v == 4]
    displays['g'], *_ = [k for k,v in rem.items() if v == 7 and k != displays['a']]
    displays['b'], *_ = set("abcdefg") - set(displays.values())
    
    reverse = {v:k for k,v in displays.items()}
    
    value = '' 
    for number in out:
        value += str(numbers[''.join(sorted(map(reverse.get, number)))])
    total += int(value) 
print("Q2:", total)


