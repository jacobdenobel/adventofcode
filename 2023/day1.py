
def get_number(line):
    digits = [x for x in line if x.isdigit()]
    return int(digits[0] + digits[-1])


def part1(data):
    return sum((digits := [int(i) for i in line if i.isdigit()])[0] * 10 + digits[-1] for line in data)

def part2(data):
    mappings = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

    for line in data

    new_data = [
        [
            x if (x := "".join([
                str(idx) for idx, val in enumerate(mappings, 1) if line[i:].startswith(val)])) 
        else line[i] for i in range(len(line))
                             
                             ] 
                             for line in data
        ]
    return part1(new_data)

if __name__ == "__main__":
    numbers = (
        ("one", 1),
        ("two", 2),
        ("three",3 ),
        ("four", 4),
        ("five", 5),
        ("six", 6),
        ("seven",7 ),
        ("eight", 8),
        ("nine", 9),
    )
    q1_total = 0
    q2_total = 0
    with open("data/1") as f:
        
        print(part2(f))
        for line in f:
            # q1_total += get_number(line)
            
            digits = [(x, i) for i, x in enumerate(line) if x.isdigit()]

            for n, d in numbers:
                try:
                    digits.append((str(d), line.index(n)))
                except ValueError:
                    continue

            digits = sorted(digits, key=lambda x:x[1])
            digits = [x[0] for x in digits]
            number = int(digits[0] + digits[-1])

            q2_total += int(number)
            
    print("Q1", q1_total)   
    print("Q2", q2_total)   