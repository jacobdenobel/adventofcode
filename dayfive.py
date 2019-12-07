
from intcode import intcode_program

if __name__ == "__main__":
    with open("inputdayfive.txt", "r") as f:
        day_five = list(map(int, f.read().strip().split(",")))
        intcode_program(day_five)
