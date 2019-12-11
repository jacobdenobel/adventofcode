from itertools import permutations
from intcode import intcode_program


if __name__ == "__main__":
    with open("inputdaytwo.txt", "r") as f:
        opcode_org = list(map(int, (f.read().split(","))))

    for noun, verb in permutations(range(0, 99), 2):
        opcode = opcode_org.copy()
        opcode[1] = noun
        opcode[2] = verb
        output = intcode_program(opcode)
        if output == 19690720:
            break

    assert noun == 22 and verb == 54   

