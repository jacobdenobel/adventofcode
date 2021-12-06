class Board:
    def __init__(self, data):
        self.n = len(data)
        self.mask = [[0] * self.n for _ in range(self.n)]
        self.lookup = dict()
        self.unmarked_sum = 0.0
        self.has_bingo = False
        for i in range(self.n):
            for j in range(self.n):
                number = data[i][j]
                self.lookup[number] = (i, j)  
                self.unmarked_sum += number

    def check(self, number):
        if number in self.lookup:
            i, j = self.lookup[number]
            self.mask[i][j] = 1
            self.unmarked_sum -= number

            if sum(self.mask[i]) == self.n:
                self.has_bingo = True
            
            if sum(x[j] for x in self.mask) == self.n:
                self.has_bingo = True

        return self.has_bingo


with open("data/day4.txt") as f:
    numbers = map(int, next(f).strip().split(","))
    boards = []
    board  = []
    for line in f:
        if not line.strip():
            if len(board):
                boards.append(Board(board))
                board = []
            continue
        board.append(list(map(int,line.strip().split())))

remaining_boards = len(boards)
for num in numbers:
    for board in boards:
        if board.has_bingo: continue
        if board.check(num):
            if remaining_boards == len(boards):
                print("Q1", board.unmarked_sum * num)
            if remaining_boards == 1: 
                print("Q2", board.unmarked_sum * num)
            remaining_boards -= 1

        
