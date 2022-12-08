def get_range(e: str) -> range:
    source, target = map(int, e.split("-"))
    return range(source, target)

def full_overlap(e1: range, e2: range) -> bool:
    if e1.start >= e2.start and e1.stop <= e2.stop:
        return True
    if e2.start >= e1.start and e2.stop <= e1.stop:
        return True
    return False

def partial_overlap(e1: range, e2: range) -> bool:
    if full_overlap(e1, e2):
        return True
    if e1.start in e2 or e1.stop in e2:
        return True
    if e2.start in e1 or e2.stop in e1:
        return True
    return False


test_data = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
""".splitlines()


if __name__ == "__main__":
    with open("data/4") as f:
        n = 0
        n2 = 0
        for line in f:
            e1, e2 = map(get_range, line.strip().split(","))
            n += int(full_overlap(e1, e2))
            n2 += int(partial_overlap(e1, e2))
    print("Q1:", n)
    print("Q2:", n2)