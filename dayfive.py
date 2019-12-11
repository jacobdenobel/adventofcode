from intcode import intcode_program

if __name__ == "__main__":
    with open("inputdayfive.txt", "r") as f:
        program = list(map(int, f.read().strip().split(",")))
        assert intcode_program(program, [1]) == 16225258
        assert intcode_program(program, [5]) == 2808771
        
