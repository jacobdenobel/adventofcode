import curses
from intcode import intcode_generator

def sign(a, b):
    if a == b:
        return 0 
    if (a - b) > 0:
        return 1
    return -1

class Display:
    MAPPER = {
        0: ' ',
        1: '|',
        2: '#',
        3: '=',
        4: '0'
    }

    def __init__(self):
        self.screen = curses.initscr()
        curses.cbreak()
        curses.noecho()
        self.tiles = dict()
        self.n_blocks = 0
        
    def update(self, state):
        for i in range(0, len(state), 3):
            x, y, tid = state[i:i+3]
            self.tiles[(x, y)] = tid
            self.n_blocks += int(tid == 2)
            if tid == 3:
                self.padx = x
            if tid == 4:
                self.ballx = x  

    def show(self, state):
        self.screen.clear()
        self.update(state)
        for (x, y), tid in self.tiles.items():
           if x== -1 and y == 0:
               self.score = tid
               self.screen.addstr(1, 45, f"Score: {tid}")
           else:
               self.screen.addstr(y, x, Display.MAPPER[tid])
        self.screen.refresh()

    def __del__(self):
        curses.napms(3000)
        curses.nocbreak()
        curses.echo()        
        curses.endwin()


class GridGame:
    def __init__(self, program, cheat=False):
        self.brain = intcode_generator(program, single=False)
        self.display = Display()
        self.cheat = cheat

    def play(self):
        key = None
        while self.step(key):
            while key not in (55, 56, 57):
                key = self.display.screen.getch()
            key -= 56
            if self.cheat:
                key = sign(self.display.ballx, self.display.padx)
            
    def step(self, key): 
        try:
            self.state = self.brain.send(key)
        except StopIteration as err:
            self.state = err.value 
        if self.state:
            self.display.show(self.state)
            return True
        return False
    
    @property
    def n_blocks(self):
        return self.display.n_blocks


def task1():
    game = GridGame(program) 
    game.play()
    assert game.n_blocks == 344
        
        
if __name__ == "__main__":
    with open("inputs/inputdaythirteen.txt", "r") as f:
        program = list(map(int, f.read().strip().split(",")))
   
    program[0] = 2
    game = GridGame(program, cheat=False) 
    game.play()  
        


