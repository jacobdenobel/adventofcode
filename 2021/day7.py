with open("data/day7.txt") as f:
    data = list(map(int, f.read().strip().split(",")))

median = sorted(data)[len(data)//2]
print("Q1:", sum(abs(x - median) for x in data))

mean = int(sum(data)/len(data))
print("Q2:", sum(sum(range(1, abs(x - mean) + 1)) for x in data))

