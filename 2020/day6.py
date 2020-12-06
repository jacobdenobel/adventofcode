from collections import Counter
if __name__ == "__main__":
    with open("data/6.txt", "r") as f:
        data = f.read().split("\n\n")
        data = [list(filter(None, d.splitlines())) for d in data]
    
    print("Q1", sum(len(set("".join(d))) for d in data))
    print("Q2", sum(sum(map(
        lambda x: 1, filter(
            lambda kv: kv[1] == len(d), Counter("".join(d)).items()
        ))) for d in data))

