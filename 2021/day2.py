import operator
from dataclasses import dataclass

@dataclass
class SubmarinePosition:
    h: int = 0
    d: int = 0 
    a: int = 0 


def f(q1 = True):
    p = SubmarinePosition()

    with open("data/day2.txt") as f:
        for line in f:
            op, k = line.strip().split()
            for operation, value in {
                    "up": [(operator.sub, "d" if q1 else "a")],
                    "down": [(operator.add, "d" if q1 else "a")], 
                    "forward": [(operator.add, "h")] + (
                        [] if q1 else [(lambda d_, k_: d_ + (p.a * k_), "d")])
                    }[op]:        
                setattr(p, value, operation(getattr(p, value), int(k)))
    return p.h * p.d

if __name__ == "__main__":
    print("Q1", f())
    print("Q2", f(False))
