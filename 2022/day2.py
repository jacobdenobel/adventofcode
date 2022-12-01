import enum

class Choice(enum.Enum):
    ROCK = 1
    PAPER = 2
    SCISSOR = 3

    @staticmethod
    def from_char(char: str) -> "Choice":
        if char in "A":
            return Choice.ROCK
        elif char in "B":
            return Choice.PAPER
        return Choice.SCISSOR

    @staticmethod
    def from_outcome(char: str, compare_to: "Choice") -> "Choice":
        if char in "X":
            return next(choice for choice in Choice if choice < compare_to)
        elif char in "Y":
            return compare_to
        return next(choice for choice in Choice if compare_to < choice)        
        

    def __lt__(self, other: "Choice") -> bool:
        if self is Choice.ROCK and other is Choice.PAPER:
            return True
        if self == Choice.PAPER and other is Choice.SCISSOR:
            return True
        if self == Choice.SCISSOR and other is Choice.ROCK:
            return True
        return False


def main():
    with open("data/2") as f:
        score = [0, 0]
        for line in f:
            op, me = line.split()
            op = Choice.from_char(op)
            for i, method in enumerate((Choice.from_char, lambda x: Choice.from_outcome(x, op))):
                mec = method(me)
                score[i] += mec.value + (3 * (op == mec))  + (6 * (op < mec))
        print("Q1:", score[0])
        print("Q2:", score[1])
            
            
if __name__ == "__main__":
    main()
