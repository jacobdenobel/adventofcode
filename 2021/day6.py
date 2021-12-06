from functools import lru_cache

@lru_cache
def f(a):
    return f(a-9) + f(a-7) if a>0 else 1

if __name__ == '__main__':
    with open("data/day6.txt") as h:
        x = list(map(int, h.read().strip().split(",")))

    print("Q1: ", sum(f(80-i) for i in x))
    print("Q1: ", sum(f(256-i) for i in x))
