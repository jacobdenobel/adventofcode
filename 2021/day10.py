def check_syntax(code, return_stack=False):
    stack = []
    for c in code:
        if c == '(':
            stack.append(')')
        elif c == '[':
            stack.append(']')
        elif c == '{':
            stack.append('}')
        elif c == '<':
            stack.append('>')
        elif stack[len(stack) - 1] == c:
            stack.pop()
        else:
            return c if not return_stack else None
    if return_stack:
        return stack

if __name__ == '__main__':
    with open("data/day10.txt") as f:
        data = [l.strip() for l in f]


    lookup = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137,
        None: 0
    }
    print("Q1:", sum(map(lookup.get, map(check_syntax, data))))

    scores = []
    for line in data:
        stack = check_syntax(line, True)
        if stack:
            s = 0 
            for c in reversed(stack):
                s *= 5
                s += (')]}>'.index(c) + 1)
            scores.append(s)
    print("Q2:", sorted(scores)[len(scores) // 2])
