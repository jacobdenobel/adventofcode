from intcode import intcode_program

if __name__ == "__main__":
    with open("inputdaynine.txt", "r") as f:
        intcode = list(map(int, f.read().strip().split(",")))

    assert intcode_program(intcode, [1]) == 2738720997
    assert intcode_program(intcode, [2]) == 50894
