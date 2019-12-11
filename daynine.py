from intcode import intcode_program

if __name__ == "__main__":
    with open("inputdaynine.txt", "r") as f:
        intcode = list(map(int, f.read().strip().split(",")))

    #intcode_program([109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99], verbose=True)
    # print()
    #intcode_program([1102,34915192,34915192,7,4,7,99,0], verbose=True)
    # print()
    #intcode_program([104,1125899906842624,99], verbose=True)
    # print()
    g = intcode_program(intcode, [1], verbose=True)
    print()

    g = intcode_program(intcode, [2], verbose=True)
