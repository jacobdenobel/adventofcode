from intcode import intcode_program

if __name__ == "__main__":
    with open("inputdayfive.txt", "r") as f:
        program = list(map(int, f.read().strip().split(",")))
        print("task1:",  intcode_program(program, [1]))
        print("task2:",  intcode_program(program, [5]))
        
