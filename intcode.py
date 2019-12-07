from operator import mul, add, lt, eq


def get_opcode(instruction):
    instruction = str(instruction)
    operation = int(instruction[-2:])
    mode1 = int(instruction[-3:-2] or 0)
    mode2 = int(instruction[-4:-3] or 0)
    mode3 = int(instruction[-5:-4] or 0)

    if operation in (3, 4):
        return operation, (mode1,)
    elif operation == 99:
        return operation, (mode1,)
    elif operation in (5, 6):
        return operation, (mode1, mode2,)
    return operation, (mode1, mode2, mode3)


def get_pos(opcode, modes, i, mi=0):
    return opcode[mi + 1] if not modes[mi] else ((i + 1) + mi)


def intcode_program(opcodes_org, inputs=None, silent=False):
    try:
        next(intcode_generator(opcodes_org, inputs))
    except StopIteration as err:
        return err.value


def intcode_generator(opcodes_org, inputs=None, parent_gen=None):
    opcodes = opcodes_org[::]
    i = 0
    output_value = opcodes[0]
    while i < len(opcodes):
        operation, modes = get_opcode(opcodes[i])
        n = len(modes) + 1
        opcode = opcodes[i:(i + n)]
        if operation == 99:
            break
        elif operation == 4:
            output_value = opcodes[get_pos(opcode, modes, i)]
        elif operation == 3:
            if not inputs:
                value = yield output_value
            else:
                value = inputs.pop(0)
            opcodes[get_pos(opcode, modes, i)] = value
        elif operation in (1, 2, 7, 8,):
            function = {
                1: add,
                2: mul,
                7: lt,
                8: eq}[operation]
            opcodes[opcode[3]] = int(function(
                opcodes[get_pos(opcode, modes, i)],
                opcodes[get_pos(opcode, modes, i, 1)],
            ))
        elif operation in (5, 6):
            if ((operation == 5 and opcodes[get_pos(opcode, modes, i)]) or
                    (operation == 6 and not opcodes[get_pos(opcode, modes, i)])):
                i = opcodes[get_pos(opcode, modes, i, 1)]
                continue
        else:
            raise NotImplementedError()
        i += n
    return output_value
