from math import ceil
from collections import defaultdict, deque

def parse_line(line): 
    source, target = line.split(" => ") 
    tquant, target = target.strip().split() 
    sources = [] 
    for source in source.split(","): 
        squant, source = source.strip().split() 
        sources.append((source.strip(), int(squant),)) 
    return target, (int(tquant), sources, ) 


def compute_amount_of_ore(reactions, n_fuel=1):
    targets = {k:v for k,v in map(parse_line, reactions)}
    _, start_reaction = targets['FUEL']
    start_reaction = [(a, q*n_fuel) for (a,q) in start_reaction]
    reaction_q = deque(start_reaction) 
    current_chem = defaultdict(lambda:0) 
    ore_c = 0 
    while any(reaction_q): 
        substance, quant = reaction_q.pop() 
        if substance == 'ORE': 
            ore_c += quant 
            continue 
        current_quant = current_chem[substance] - quant 
        if current_quant < 0: 
            sam, substance_react = targets[substance] 
            n_times = ceil(abs(current_quant) / sam) 
            reaction_q.extend([(a, q*n_times) for (a,q) in substance_react]) 
            current_chem[substance] += ((sam*n_times) -quant) 
        else: 
            current_chem[substance] -= quant
    return ore_c

def compute_amount_of_fuel(reactions, am_ore):
    ore_one_f = compute_amount_of_ore(reactions)
    target = ore_one_f // am_ore
    ore_f = compute_amount_of_ore(reactions, n_fuel=target) 
    while ore_f < am_ore: 
        target += (am_ore-ore_f) // ore_one_f + 1
        ore_f = compute_amount_of_ore(reactions, n_fuel=target)
    return target - 1


if __name__ == "__main__":
    testcase1 = [
        "10 ORE => 10 A",
        "1 ORE => 1 B",
        "7 A, 1 B => 1 C",
        "7 A, 1 C => 1 D",
        "7 A, 1 D => 1 E",
        "7 A, 1 E => 1 FUEL"       
    ]
    assert compute_amount_of_ore(testcase1) == 31
    
    testcase2 = [
        '9 ORE => 2 A',
        '8 ORE => 3 B',
        '7 ORE => 5 C',
        '3 A, 4 B => 1 AB',
        '5 B, 7 C => 1 BC',
        '4 C, 1 A => 1 CA',
        '2 AB, 3 BC, 4 CA => 1 FUEL'
    ]
    assert compute_amount_of_ore(testcase2) == 165
    testcase3 = [
        '157 ORE => 5 NZVS',
        '165 ORE => 6 DCFZ',
        '44 XJWVT, 5 KHKGT, 1 QDVJ, 29 NZVS, 9 GPVTF, 48 HKGWZ => 1 FUEL',
        '12 HKGWZ, 1 GPVTF, 8 PSHF => 9 QDVJ',
        '179 ORE => 7 PSHF',
        '177 ORE => 5 HKGWZ',
        '7 DCFZ, 7 PSHF => 2 XJWVT',
        '165 ORE => 2 GPVTF',
        '3 DCFZ, 7 NZVS, 5 HKGWZ, 10 PSHF => 8 KHKGT',
    ]
    assert compute_amount_of_ore(testcase3)== 13312

    with open("inputs/inputdayfourteen.txt", "r") as f:
        reactions = f.readlines()
        assert compute_amount_of_ore(reactions) == 399063
    assert compute_amount_of_fuel(reactions, 1000000000000) == 4215654


