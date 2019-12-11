from collections import defaultdict
from intcode import intcode_program


def run_robot(program, start_color=0):
    direction = 1
    painted_panels = defaultdict(lambda: 0)
    robot = intcode_program(program, verbose=False)
    pos = [0,0]
    painted_panels[tuple(pos)] = start_color

    while True:
        try:
            color, next_direction = robot.send(painted_panels[tuple(pos)])
            painted_panels[tuple(pos)] = color
            if next_direction:
                direction += 1
            else:
                direction -= 1

            if direction < 0:
                direction = 3
            elif direction > 3:
                direction = 0

            if direction == 0:
                pos[0] -= 1
            elif direction == 1:
                pos[1] += 1
            elif direction == 2:
                pos[0] += 1
            elif direction == 3:
                pos[1] -= 1
        except StopIteration:
            print("Completed. Painted {} panels.".format(len(painted_panels.keys())))
            break       
    
    return painted_panels


if __name__ == "__main__":
    with open("inputs/inputdayeleven.txt", "r") as f:
        program = list(map(int,f.read().strip().split(',')))
    
    # task1 
    run_robot(program)

    # task2
    panels = run_robot(program, start_color=1)
    
    for line in ["".join([ "#" if panels[tuple([i, x])] else " " 
        for i in range(0, max(list(panels.keys()), key=lambda x:x[0])[0])])     
        for x in range(min(list(panels.keys()), key=lambda x:x[1])[1], 1)][::-1]:
        print(line)
    

