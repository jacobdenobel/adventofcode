from math import sqrt, isclose, degrees, atan2
from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])

def distance(a, b):
    return sqrt((a.x - b.x) ** 2 + (a.y - b.y)**2)


def is_between(a, c, b):
    return isclose(distance(a,c) + distance(c,b), distance(a,b))


def get_markers(grid, marker="#"):
    return [Point(x, y) 
            for y, row in enumerate(grid)
            for x, pos in enumerate(row) 
            if pos == marker
            ]

def get_asteriods(grid):
    return get_markers(grid)

def get_station(grid):
    return next(iter(get_markers(grid, marker="X")), None)


def compute_visible_asteriods(A, Ac):
    return {
        a: list(filter(None,[ 
            ax if not any(
                [is_between(a, ay, ax) for ay in A if ay not in (a, ax)]
            ) else None
            for ax in A if ax != a 
         ])) 
        for a in Ac  
    }

def task1(grid):
    A = get_asteriods(grid)
    A = compute_visible_asteriods(A, A)
    max_a = max(A, key=lambda x:len(A.get(x)))
    return max_a, len(A[max_a])


def run_tests_task1():
    testcase1 = [
            ".#..#",
            ".....",
            "#####",
            "....#",
            "...##"
        ]
    a, n = task1(testcase1)
    assert a == Point(3,4) and n == 8

    
    testcase2 = [
        '......#.#.',
        '#..#.#....',
        '..#######.',
        '.#.#.###..',
        '.#..#.....',
        '..#....#.#',
        '#..#....#.',
        '.##.#..###',
        '##...#..#.',
        '.#....####'    
    ]
    a, n = task1(testcase2)
    assert a == Point(5,8) and n == 33

    testcase3 = [
        '#.#...#.#.',
        '.###....#.',
        '.#....#...',
        '##.#.#.#.#',
        '....#.#.#.',
        '.##..###.#',
        '..#...##..',
        '..##....##',
        '......#...',
        '.####.###.'
        ]

    a, n = task1(testcase3)
    assert a == Point(1,2) and n == 35

    testcase4 = [
        '.#..#..###',
        '####.###.#',
        '....###.#.',
        '..###.##.#',
        '##.##.#.#.',
        '....###..#',
        '..#.#..#.#',
        '#..#.#.###',
        '.##...##.#',
        '.....#.#..']

    a, n = task1(testcase4)
    assert a == Point(6,3) and n == 41 

    testcase5 = [
        '.#..##.###...#######',
        '##.############..##.',
        '.#.######.########.#',
        '.###.#######.####.#.',
        '#####.##.#.##.###.##',
        '..#####..#.#########',
        '####################',
        '#.####....###.#.#.##',
        '##.#################',
        '#####.##.###..####..',
        '..######..##.#######',
        '####.##.####...##..#',
        '.#####..#.######.###',
        '##...#.##########...',
        '#.##########.#######',
        '.####.#.###.###.#.##',
        '....##.##.###..#####',
        '.#.#.###########.###',
        '#.#.#.#####.####.###',
        '###.##.####.##.#..##']
    a, n = task1(testcase5)
    assert a == Point(11,13) and n == 210




def task2(grid, print_a=[], station=None):
    A = get_asteriods(grid)
    station = station or get_station(grid)
    if station in A:
        A.remove(station)
    c = 0
    while any(A):
        visible = compute_visible_asteriods(A, [station])
        da = {
            p: degrees(atan2(p.y-station.y, p.x-station.x)) 
            for p in visible[station]
        }
        order = sorted(
                [(k, v+90 if v+90 >= 0 else 360+(90+v)) for k,v in da.items()],
                key=lambda x:x[1]
            )
        for asteriod, angle in order:
            A.remove(asteriod)
            c += 1
            if c in print_a:
                print(c, asteriod)
    return c
    

def test_task2():
    testcase1 = [
        '.#....#####...#..',
        '##...##.#####..##',
        '##...#...#.#####.',
        '..#.....X...###..',
        '..#.#.....#....##'
    ]
    task2(testcase1, [5, 9])
    
    testcase5 = [
        '.#..##.###...#######',
        '##.############..##.',
        '.#.######.########.#',
        '.###.#######.####.#.',
        '#####.##.#.##.###.##',
        '..#####..#.#########',
        '####################',
        '#.####....###.#.#.##',
        '##.#################',
        '#####.##.###..####..',
        '..######..##.#######',
        '####.##.####...##..#',
        '.#####..#.######.###',
        '##...#.##########...',
        '#.##########.#######',
        '.####.#.###.###.#.##',
        '....##.##.###..#####',
        '.#.#.###########.###',
        '#.#.#.#####.####.###',
        '###.##.####.##.#..##'
    ]
    task2(testcase5, [1, 2, 10, 200, 299], Point(11,13))





if __name__ == "__main__":
    with open("inputdayten.txt", "r") as f:
        grid = [x.strip() for x in f]

    station, n= task1(grid)
    task2(grid, [200], station)
    
        
    
    

