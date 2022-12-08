import string

test_data = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
""".splitlines()




if __name__ == "__main__":
    with open("data/3") as f:
        prio = 0
        badge_prio = 0
        groups = []
        for i, line in enumerate(f):
            line = line.strip()
            groups.append(set(line))
            if len(groups) == 3:
                intsec = groups[0]
                for g in groups[1:]:
                    intsec = intsec.intersection(g)
                for item in intsec:
                    badge_prio += (string.ascii_letters.index(item) + 1) 
                groups = []

            n = len(line)//2
            cmp1, cmp2 = set(line[:n]), set(line[n:])
            for item in cmp1.intersection(cmp2):
                prio += (string.ascii_letters.index(item) + 1)

    print("Q1:", prio)
    print("Q1:", badge_prio)