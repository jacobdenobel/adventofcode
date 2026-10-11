from dataclasses import dataclass, field
from itertools import combinations

@dataclass
class Box:
    x: int
    y: int
    z: int

    def distance(self, other: "Box"):
        squared_error = (
              pow(self.x - other.x, 2) 
            + pow(self.y - other.y, 2) 
            + pow(self.z - other.z, 2)
        )
        return pow(squared_error, .5)
    

@dataclass
class Circuit:
    boxes: list = field(default=None)


class Combinations:
    def __init__(self, boxes):
        self.combs = list(combinations(boxes, 2))
        self.distances = [b1.distance(b2) for b1, b2 in self.combs]
        self.combined = []
    
    def __iter__(self):
        self.i = -1
        return self
    
    def __next__(self):
        while self.i not in self.combined:
            self.i += 1
        return self.i, self.combs[self.i], self.distances[self.i]




def load_data(fname):
    data = []
    with open(fname) as f:
        for line in f:
            data.append(Box(*map(int, line.strip().split(","))))
        return data
    

def min_distance(boxes: list[Box]):
    min_d = float("inf")
    min_c = None
    for i, b1, b2, dist in combinations(boxes, 2):
        if dist < min_d:
            min_c = (b1, b2)
            min_d = dist

    return min_c, min_d
    

if __name__ == "__main__":
    boxes = load_data("data/8_test")
    combinations = Combinations(boxes)

    closest_pair, dist = min_distance(boxes)
    circuits = [Circuit(closest_pair)]
    print(circuits)
