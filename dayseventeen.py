import re
from time import sleep
from collections import defaultdict, deque, Counter
from itertools import permutations

from intcode import intcode_program, intcode_generator



class Robot:
    robot_ints = list(map(ord,"<>v^"))

    def __init__(self, program):
        self.program = intcode_generator(program, single=False)
        self.set_state()

        self.path = self.get_command_path()
        self.ngrams = self.compute_ngrams(self.path) 
        self.main, self.A, self.B, self.C = self.find_compression(
                self.path, self.ngrams)

    def run(self, feed=True):
        self.display()
        feed = [ord('y') if feed else ord('n')] + [10]
        for command in (self.main, self.A, self.B, self.C, feed,):
            for digit in self.make_ascii(command):
                try:
                    self.state = self.program.send(digit)
                except StopIteration as err:
                    print("stop")
                    self.state = err.value
            breakpoint()
            self.display()
            sleep(1)


    def set_state(self):
        try: 
            self.state = next(self.program)
        except StopIteration as err:
            self.state = err.value
    
        self.state_dict = self.make_state_dict()
        self.edgelist = self.make_edgelist()

    def make_state_dict(self):
        i, j = 0, 0
        state = dict()
        for char in self.state:
            if char == 10:
                j+=1
                i = 0
            else:
                state[(i, j)] = char
                i += 1
        return state

    
    def make_edgelist(self):
        edgelist = defaultdict(list)
        scaffold_ints = [35] + self.robot_ints
        for pos, char in self.state_dict.items():
            if char in scaffold_ints:
                for npos in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    npos = (pos[0] + npos[0], pos[1] + npos[1], )
                    if self.state_dict.get(npos) in scaffold_ints:
                        edgelist[pos].append(npos)
        return edgelist


    @property
    def pos(self):
        return next(filter(lambda x: x[1] in self.robot_ints, 
            self.state_dict.items()))[0]

    def traverse(self):
        ori = 'up'
        pos = self.pos
        while True:
            neighs = self.edgelist.get(pos)
            moves = [self.get_move(ori, pos, n) for n in neighs]
            move = next(filter(lambda x:x[1] == ['R'], moves), None)
            move = next(filter(lambda x:x[1] == ['L'], moves), None) or move
            move = next(filter(lambda x:x[1] == ['X'], moves), None) or move
            if not move:
                return 
            if move[1] == ['X']:
                pos = neighs[moves.index(move)]
            ori, move = move
            yield move[0], pos

    def get_command_path(self):
        return ''.join(self.format_path(map(lambda x:x[0], self.traverse())))    

    def format_path(self, command_path):
        command_path = list(command_path)
        path = []
        n = 0
        for c in command_path:
            if c != 'X':
                if n:
                    path.append(str(n))
                    n = 0
                path.append(c)
            else:
                n += 1
        else:
            path.append(str(n))
        return path
    
    def get_move(self, orientation, current_node, next_node):
        d = ['left', 'up', 'right', 'down']
        try:
            should_go = {
                (0, -1): 'up',
                (0,  1): 'down',
                (1,  0): 'right',
                (-1, 0): 'left'
            }[(next_node[0] - current_node[0], next_node[1] - current_node[1],)]
        except:
            breakpoint()
        if should_go == orientation:
            return should_go, ['X']
        

        d = d[d.index(orientation)+1:] + d[:d.index(orientation)]
        n_right = 0
        for di in d:
            n_right += 1
            if di == should_go:
                break

        n_left = 0
        for di in reversed(d):
            n_left += 1
            if di == should_go:
                break 
        if n_left < n_right:
            return should_go, ['L'] * n_left
        return should_go, ['R'] * n_right

    def compute_ngrams(self, path, check_strings=None):
        check_strings = check_strings or [path]
        ngrams = Counter()
        for i in range(6, 12):
            for j in range(len(path)-i):
                ngram = path[j:j+i]
                ngrams[ngram] = sum((x.count(ngram) for x in check_strings))
        return ngrams

    
    def compress(self, path, A, B, C):
        path = re.sub(C, 'C', re.sub(B, 'B', re.sub(A, 'A', path)))
        return path


    def drive(self):
        old_pos = self.pos
        for move, new_pos in self.traverse():
            self.state[old_pos[0] + (old_pos[1]*42)] = 35
            self.state[new_pos[0] + (new_pos[1]*42)] = 62
            old_pos = new_pos
            self.display()
            sleep(.1)

    def find_compression(self, path, ngrams_):
        ngrams = map(lambda x:x[0], filter(lambda x:x[1] > 0, ngrams_.most_common()))
        best = float("inf")
        for A, B, C in permutations(ngrams, 3):
            new_path = self.compress(path, A, B, C)
            if len(new_path) <= 11:
                return new_path, A, B, C
            if best > len(new_path):
                np = new_path
                best =len(new_path)
                a,b,c = A,B,C
        return np, a,b,c 
        breakpoint()
        raise Exception("No compression found")
    
    def make_ascii(self, code):
        ascii_code = []
        for char in code:
            ascii_code.extend([ord(char), ord(",")])
        ascii_code[-1] = 10
        return ascii_code

    def display(self):    
        for char in self.state:
            print(chr(char), end='')
   

def question1(pogram):
    robot = Robot(program)
    intersections = filter(lambda x: len(robot.edgelist[x]) == 4, 
            robot.edgelist.keys()) 
    return sum((x[0] * x[1] for x in intersections))

if __name__ == "__main__":
    with open("inputs/inputdayseventeen.txt", "r") as f:
        program = list(map(int,f.read().strip().split(',')))
    
    assert question1(program) == 7584
    program[0] = 2 
    robot = Robot(program)

    # This should work
    #robot.run()

