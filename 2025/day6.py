
def product(vec):
    total = 1
    for xi in vec:
        total *= xi
    return total


def reformat(data):
    l = len(data[0])
    d = []
    for i in range(l):
        number = ''.join(d[i] for d in data[::-1])
        d.insert(0, int(number.strip()))
    return d


# data = []
# with open("data/6_test") as f:
#     for line in f:
#         line = list(filter(None, line.strip().split()))
#         if line[0].isdigit():
#             data.append(list(map(int, line)))
#         else:
#             data = list((zip(*data)))
#             total = 0
#             for i, op in enumerate(line):
#                 if op == '+':
#                     value = sum(data[i])
#                 else:
#                     value = product(data[i])
#                 total += value
#             print(total)



data = []
widths = []
total = 0
with open("data/6") as f:
    for i, line in enumerate(reversed(f.read().split("\n"))):
        if i == 0:
            ops = line.strip().split()
            w = 0
            for c in line[1:]:
                if c == ' ':
                    w += 1
                else:
                    widths.append(w)
                    w = 0
            widths.append(w+1)
            continue
    
        row = []
        i = 0
        for w in widths:
            row.append(line[i:i+w])
            i+=w+1
        data.append(row)

    data = list((zip(*data)))
    for x, op in zip(data, ops):
        x = reformat(x)
        if op == '+':
            value = sum(x)
        else:
            value = product(x)
        print(op, x, value)
        total += value

print(total)    
