def detect(data, n=4):
    for i in range(n, len(data)):
        if len(set(data[i-n:i])) == n:
            return i, data[i-n:i]
        

with open("data/6") as f:
    data = f.read().strip()
    print("Q1", detect(data))
    print("Q2", detect(data, 14))

