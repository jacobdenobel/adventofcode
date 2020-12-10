def check_preamble(data, preamble_size=25):
    incorrect = []
    for i in range(preamble_size, len(data)):
        preamble = set(data[i-preamble_size:i])
        number = data[i]
        for e in preamble:
            delta = number - e
            if delta in preamble:
                break
        else:
            incorrect.append(number)
    return incorrect

def find_max_contiguous_sequence(data, sum_to):
    r, m = [], []
    for e in filter(lambda x: x < sum_to, data):
        r.append(e)
        while sum(r) > sum_to:
            r.pop(0)
        if sum(r) == inc and len(r) > len(m):
            m = r.copy()
    return m


if __name__ == "__main__":
    with open("data/9.txt") as f:
        data = list(map(int, f))
    inc, *_ = check_preamble(data)
    print("Q1", inc)
    seq = find_max_contiguous_sequence(data, inc)
    print("Q2", min(seq) + max(seq))

