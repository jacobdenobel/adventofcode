import itertools

def sign(x):
    return (x > 0) - (x < 0)

def run_probe(dx, dy):
    x, y = 0, 0
    while True:
        x += dx
        y += dy
        dx -= sign(dx)
        dy -= 1
        yield x, y

def brute_force(xr, yr, T=500):
    T = T or max(max(xr), abs(min(yr)))
    xrange = range(xr[0], xr[1] + 1)
    yrange = range(yr[0], yr[1] + 1)
    hits = set()
    possible_values =  range(
        min(min(yr), min(xr)) - 1, 
        max(max(xr), abs(min(yr))) + 1
    )
    for dx, dy in itertools.chain(
        itertools.permutations(possible_values, 2), 
        map(lambda x:(x, x), possible_values)
    ):
        maxy = -float("inf")
        for t, (x, y) in zip(range(T), run_probe(dx, dy)):
            maxy = max(y, maxy)
            if y in yrange and x in xrange:
                hits.add((dx, dy, maxy))
    return hits


if __name__ == "__main__":
    test1 = "target area: x=20..30, y=-10..-5"
    test1 = open("data/day17.txt").read()
    xrange, yrange = map(
        lambda x: tuple(map(int, x.split("=")[1].split(".."))),
        test1.replace(",", "").split()[2:],
    )

    hits = brute_force(xrange, yrange)
    print("Q1:", max(hits, key=lambda x: x[-1])[-1])
    print("Q2:", len(hits))

