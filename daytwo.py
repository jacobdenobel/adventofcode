from operator import mul, add
from itertools import permutations 

with open("inputdaytwo.txt", "r") as f:
    optcodes_org = list(map(int, (f.read().split(","))))



def intcode(noun, verb):
    optcodes = optcodes_org[::]
    optcodes[1] = noun
    optcodes[2] = verb
    for i in range(0, len(optcodes), 4):
        optcode = optcodes[i:i+4]
        if optcode[0] == 99:
            break
        function = mul if optcode[0] == 2 else add
        optcodes[optcode[3]] = function(
            optcodes[optcode[1]], optcodes[optcode[2]])

    return optcodes[0]

for noun, verb in permutations(range(0, 99), 2):
    output = intcode(noun, verb)
    if output == 19690720:
        print(noun, verb)
        break

    

