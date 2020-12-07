def traverse(g, start, unique=True):
    stack = [start]
    seen = list()
    while len(stack) > 0:
        node = stack.pop()
        seen.append(node)
        value = g[node]
        if not value or not value[0]:
            continue

        for n, key in value:
            n = n if not unique else 1
            stack.extend([key for _ in range(int(n))])
    return seen


if __name__ == "__main__":
    with open('data/7.txt') as f:
        g = dict()
        for key, value in map(lambda x: x.split("bags contain"), f):
            value = value.replace(",", "").replace("bags", "bag").split("bag")
            value = filter(lambda x: len(x) > 2, map(str.strip, value))
            g[key.strip()] = list(map(lambda x: tuple(x.split(maxsplit=1))
                                  if x != 'no other' else None, value))

    SG = 'shiny gold'
    q1_keys = filter(lambda x: x != SG, g.keys())

    print("Q1", sum(1 for key in q1_keys if SG in traverse(g, key)))
    print("Q2", len(traverse(g, SG, unique=False)) - 1)


