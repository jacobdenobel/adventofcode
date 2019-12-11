from operator import mul, add, lt, eq


def get_opcode(instruction):
    instruction = str(instruction)
    operation = int(instruction[-2:])
    mode1 = int(instruction[-3:-2] or 0)
    mode2 = int(instruction[-4:-3] or 0)
    mode3 = int(instruction[-5:-4] or 0)

    if operation in (3, 4, 9):
        return operation, (mode1,)
    elif operation == 99:
        return operation, (mode1,)
    elif operation in (5, 6):
        return operation, (mode1, mode2,)
    return operation, (mode1, mode2, mode3)


def get_pos(opcode, modes, i, rb, mi=0):
    mode = modes[mi]
    if not mode:
        return opcode[mi + 1]
    elif mode is 1:
        return (i + 1) + mi
    elif mode is 2:
        return rb + opcode[mi + 1]


def intcode_program(opcodes_org, inputs=None, verbose=False):
    try:
        g = intcode_generator(opcodes_org, inputs, verbose=verbose)
        next(g)
    except StopIteration as err:
        return err.value
    else:
        return g


def increase_memory(opcodes, new_index):
    return opcodes + ([0] * ((new_index + 1) - len(opcodes)))


def intcode_generator(opcodes_org, inputs=None, verbose=True):
    opcodes = opcodes_org[::]
    relative_base = 0
    i = 0
    output_value = opcodes[0]
    while i < len(opcodes):
        operation, modes = get_opcode(opcodes[i])
        if operation == 99:
            break
        n = len(modes) + 1
        opcode = opcodes[i:(i + n)]
        p1 = get_pos(opcode, modes, i, relative_base)
        p2 = get_pos(opcode, modes, i, relative_base, 1) if n > 2 else None
        p3 = get_pos(opcode, modes, i, relative_base, 2) if n == 4 else None
        for p in (p1, p2, p3):
            if p and p > len(opcodes) - 1:
                opcodes = increase_memory(opcodes, p)
        if operation == 4:
            output_value = opcodes[p1]
            if verbose:
                print(output_value)
        elif operation == 3:
            if not inputs:
                value = yield output_value
            else:
                value = inputs.pop(0)
            opcodes[p1] = value
        elif operation in (1, 2, 7, 8,):
            opcodes[p3] = int({
                1: add,
                2: mul,
                7: lt,
                8: eq}[operation](opcodes[p1], opcodes[p2]))

        elif operation in (5, 6):
            if ((operation == 5 and opcodes[p1]) or
                    (operation == 6 and not opcodes[p1])):
                i = opcodes[p2]
                continue
        elif operation == 9:
            relative_base += opcodes[p1]
        else:
            raise NotImplementedError()
        previous_opcode = opcode
        i += n
    return output_value
