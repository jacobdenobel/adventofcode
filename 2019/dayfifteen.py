import random

from time import sleep
from collections import defaultdict, deque
from intcode import intcode_program


NORTH = 1
SOUTH = 2
WEST = 3
EAST = 4

DIRECTIONS = [
    NORTH,
    SOUTH,
    WEST,
    EAST
]

REVERSE_DIRECTIONS = [
    SOUTH,
    NORTH,
    EAST,
    WEST
]

class Robot:
    STR_MAPPER = ['#', ' ', 'O', '?']
    def __init__(self, program):
        self.pos = 0,0
        self.program = intcode_program(program)
        self.stack = deque([self.pos])
        self.target = None
        self.seen = dict()
        self.t = 0

    def get_next_pos(self, direction, pos=None):
        pos = pos or self.pos
        if direction == NORTH:
            return (pos[0], pos[1] + 1,)
        elif direction == SOUTH:
            return (pos[0], pos[1] - 1,)
        elif direction == EAST:
            return (pos[0] + 1, pos[1],)
        elif direction == WEST:
            return (pos[0] - 1, pos[1],)

    def get_next_direction(self, pos, opos=None):
        for direction in DIRECTIONS:
            if self.get_next_pos(direction, opos) == pos:
                return direction

    def search(self):
        path = []
        while len(self.stack):
            self.t += 1
            v = self.stack.pop() 
            if v is not self.pos:
                reverse_path = path[::-1]
                for i, pv in enumerate(reverse_path):
                    next_direction = self.get_next_direction(v)
                    if next_direction:
                        assert self.program.send(next_direction)[0] in [1,2]
                        self.pos = v
                        break            
                    nd = self.get_next_direction(pv)
                    if not nd: 
                        continue
                    assert self.program.send(nd)[0] in [1,2]
                    self.pos = self.get_next_pos(nd)   
            path.append(self.pos)
            if not self.seen.get(v):
                self.seen[v] = ' ' 
                for direction, reverse in zip(DIRECTIONS, REVERSE_DIRECTIONS):
                    pos = self.get_next_pos(direction)
                    status_code = self.program.send(direction)[0]
                    if status_code == 0:
                        self.seen[pos] = '#'
                        continue
                    if not self.seen.get(pos):
                        self.stack.append(pos)
                    if status_code == 2:
                        self.seen[pos] = 'G'
                    assert self.program.send(reverse)[0] in [1, 2]
   
        return self

    def path(self, v):
       count = 0
       while self.reverse.get(v):
            count += 1
            v = self.reverse.get(v)
       return count


    def longest_path(self):
        max_ = 0
        for node in self.reverse:
            max_ = max(self.path(node), max_) 
        return max_


    def solve(self, reverse=False):
        if not reverse:
            pos = (0,0,)
        else:
            pos = next(iter([x for x,y in robot.seen.items() if y =='G']))
        Q = deque([pos])
        seen = {pos}
        self.reverse = {}
        while len(Q) != 0:
            v = Q.pop()
            self.pos = v
            if self.seen[v] == 'G' and not reverse:
                return self.path(v)
            for d in DIRECTIONS:
                w = self.get_next_pos(d)
                if w not in seen and self.seen.get(w) is not '#':
                    seen.add(w)
                    Q.append(w)
                    self.reverse[w] = v
        return self.longest_path()        
   
    def display(self):    
        print()
        for y in range(-25, 25):
            for x in range(-25, 25):
                if (x,y,) == self.pos:
                    print("&", end="")
                else:
                    print(self.seen.get((x, y)) or "?", end='')
            print(f" {y}\n", end='')
        print()
    

if __name__ == "__main__":
    with open("inputs/inputdayfifteen.txt", "r") as f:
        program = list(map(int,f.read().strip().split(',')))
    
    robot = Robot(program).search()
    assert robot.solve() == 280
    assert robot.solve(reverse=True) == 400
        

