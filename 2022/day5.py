from collections import defaultdict

stacks = defaultdict(list)

if __name__ == "__main__":
    with open("data/5") as f:
        init = True
        q1 = True
        for line in f:
            line = line.strip()
            if not line:
                init = False
                continue

            if init:
                idx = 1
                for i, c in enumerate(line): 
                    if i % 4 == 1:
                        if c != ' ':
                            stacks[idx].append(c)
                        idx += 1
                continue

            n, idx, to = map(int, filter(str.isdigit, line.split()))
            
            for i in range(n):
                if q1:
                    i = 0
                stacks[to].insert(i, stacks[idx].pop(0))
    
    print("".join(stacks[i][0] for i in sorted(stacks.keys())))
        