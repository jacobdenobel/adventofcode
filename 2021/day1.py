def iter_file(k=3):
    with open("data/day1.txt") as f:
        window = [int(next(f)) for _ in range(k)]
        yield window
        for line in f:
            window = window[1:] + [int(line)]
            yield window

if __name__ == "__main__":
    print("Q1", sum(map(lambda pc: pc[1] > pc[0], iter_file(2))))
    print("Q2", sum(map(lambda pc: sum(pc[1:]) > sum(pc[:-1]), iter_file(4))))

