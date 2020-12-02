from itertools import combinations

with open("data/1.txt", "r") as f:
    data = list(map(int, f.readlines()))


for a,b in combinations(data, 2):
    if a + b == 2020:
        print(a*b)

for a,b,c in combinations(data, 3):
    if a + b + c == 2020:
        print(a*b*c)

