from collections import Counter


with open("data/1") as t:
    lefts, rights = [], []
    for line in t:
        left, right = map(int, line.strip().split())
        lefts.append(left)
        rights.append(right)
    lefts.sort()
    rights.sort()
    distance = 0
    similarity = 0
    right_counts = Counter(rights)
    for left, right in zip(lefts, rights):
        distance += abs(left - right)
        similarity += left * right_counts.get(left, 0)
    print("q1", distance)
    print("q1", similarity)

