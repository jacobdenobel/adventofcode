import itertools

BASE_PATTERN = [0, 1, 0, -1]

def get_pattern(pos):
    pattern = []
    for p in BASE_PATTERN:
        pattern.extend([p] * (pos + 1))
    pattern = itertools.cycle(pattern)
    next(pattern)
    return pattern

def apply_pattern(pos, sequence):
    pattern = get_pattern(pos)
    result = sum((s*p for s,p in zip(sequence, pattern)))
    return int(str(result)[-1])

def apply_phase(sequence):
    return [apply_pattern(p, sequence) for p in range(len(sequence))]

def compute_output(sequence, n_phases=100):
    for _ in range(n_phases):
        sequence = apply_phase(sequence)
    return ''.join(map(str, sequence[:8]))


def compute_output2(sequence):
    offset = int(''.join(map(str, sequence[:7])))
    sequence = (sequence*10000)[offset:]
    for _ in range(100):
        suffix_sum = 0
        for i in range(len(sequence)-1, -1, -1):
            sequence[i] = suffix_sum = (suffix_sum + sequence[i]) % 10
    return ''.join(map(str, sequence[:8]))


if __name__ == "__main__":
    with open("inputs/inputdaysixteen.txt", "r") as f:
        sequence = list(map(int, f.read().strip()))

    assert compute_output([1,2,3,4,5,6,7,8], n_phases=4) == '01029498'
    assert compute_output(
            list(map(int, '80871224585914546619083218645595'))
        ) == '24176176'
    assert compute_output(
            list(map(int, '19617804207202209144916044189917'))    
        ) == '73745418'
    assert compute_output(
            list(map(int, '69317163492948606335995924319873'))    
        ) == '52432133'

    
    print("Question 1:\t", compute_output(sequence))
    print("Question 2:\t", compute_output2(sequence))
    

