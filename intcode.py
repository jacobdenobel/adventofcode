from operator import mul, add, lt, eq


def get_positions(opcodes, instruction, i, rb, n):
    def inner(mi, opcodes=opcodes, instruction=instruction, i=i, rb=rb, n=n):
        if (mi == 1 and n < 3) or (mi == 2 and n != 4): 
            return None
        opcode = opcodes[i:(i + n)]
        mode = int(instruction[-(3+mi):-(2+mi)] or 0)
        pos = opcode[mi+1] if not mode else (
            (i+1+mi) if mode is 1 else (rb+opcode[mi+1])
        )
        if pos > len(opcodes) - 1:
            opcodes += ([0] * ((pos + 1) - len(opcodes)))
        return pos
    return list(map(inner, range(0, 3)))


def intcode_generator(opcodes_org, verbose=False):
    opcodes = opcodes_org.copy()
    rb, i  = 0, 0
    output_values = []
    while i < len(opcodes):
        instruction = str(opcodes[i])
        operation = int(instruction[-2:])
        if operation == 99: break
        n = 1 + (1 if operation in (3, 4, 9,) else (
            2 if operation in (5, 6,) else 3)
            ) 
        p = get_positions(opcodes, instruction, i, rb, n)
        if operation == 4:
            output_values.append(opcodes[p[0]])
            if verbose: print(output_values[-1])
        elif operation == 3:
            value = yield output_values
            output_values = []
            if verbose: print("Got", value)
            opcodes[p[0]] = value
        elif operation in (1, 2, 7, 8,):
            opcodes[p[2]] = int({
                1: add,
                2: mul,
                7: lt,
                8: eq}[operation](opcodes[p[0]], opcodes[p[1]]))
        elif operation in (5, 6):
            if ((operation == 5 and opcodes[p[0]]) or
                    (operation == 6 and not opcodes[p[0]])):
                i = opcodes[p[1]]
                continue
        elif operation == 9:
            rb += opcodes[p[0]]
        else:
            raise NotImplementedError()
        i += n
    return next(iter(output_values[::-1]), opcodes[0])


def intcode_program(opcode, inputs=[], **kwargs):
    try:
        g = intcode_generator(opcode, **kwargs)
        for i in [None] + inputs:
            g.send(i)
    except StopIteration as err:
        return err.value
    else:
        return g


