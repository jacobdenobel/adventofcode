from collections import Counter

def get_indices(iterable, item):
    return [i for i, x in enumerate(iterable) if x == item]


total = 0                  
with open('data/7') as f:
    for i, line in enumerate(f):
        line = line.strip()
        if i == 0:
            beams = Counter(get_indices(line, "S"))
            continue
        
        splitters = get_indices(line, "^")        

        new_beams = Counter()
        for pos, count in beams.items():
            if pos in splitters:
                total += 1

                if pos > 0:
                    new_beams[pos - 1] += count
                
                if pos < len(line) -1:
                    new_beams[pos + 1] += count
            else:
                new_beams[pos] += count

        beams = new_beams

    print(total, sum(beams.values()))


        
    