from copy import deepcopy


def to_lowest_level(x, depth=0, previous_level=None, allow_split=False):
    if previous_level is None:
        previous_level = []
    
    if isinstance(x[0], list):
        return to_lowest_level(x[0], depth+1, previous_level + [x],  allow_split)
    
    if isinstance(x[1], list):
        return to_lowest_level(x[1], depth+1, 0 + [x],  allow_split)

    if depth == 4:
        explode(x, previous_level, allow_split)

    return previous_level[0]


def inc_leftmost(xx, pos, d):
    if isinstance(xx[pos], list):
        inc_leftmost(xx[pos], 0, d)
        return 
    xx[pos] += d

def inc_rightmost(xx, pos, d):
    if isinstance(xx[pos], list):
        inc_leftmost(xx[pos], -1, d)
        return 
    xx[pos] += d

def explode(x, previous_level, allow_split):
    container = previous_level[-1]
    pos = container.index(x)

    container[pos] = 0
    if pos > 0:    
        container[pos - 1] += x[0]
    else:
        cc = container
        for i, lvl in enumerate(previous_level[:-1][::-1]):
            if lvl.index(cc) != 0:
                inc_rightmost(lvl, lvl.index(cc)-1, x[0])
                break
            cc = lvl

    if pos != (len(container) -1):  
        container[pos + 1] += x[1]
    else:
        cc = container
        for i, lvl in enumerate(previous_level[:-1][::-1]):
            if lvl.index(cc) != (len(lvl)-1):
                inc_leftmost(lvl, lvl.index(cc)+1, x[1])
                break
            cc = lvl

    if allow_split:
        # breakpoint()
        pass

def reducer(x):
    x1 = to_lowest_level(deepcopy(x))
    x2 = to_lowest_level(deepcopy(x)[::-1])[::-1]
    breakpoint()
    


if __name__ == '__main__':
    data = []
    with open("data/day18.test.txt") as f:
        for line in f:
            data.append(eval(line.strip()))

    ex1 = eval('[[[[[9,8],1],2],3],4]')
    print(reducer(ex1))

    ex1 = eval('[7,[6,[5,[4,[3,2]]]]]')
    print(reducer(ex1))

    ex1 = eval('[[6,[5,[4,[3,2]]]],1]')
    print(reducer(ex1))

    ex1 = eval('[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]')
    print(reducer(ex1))

    ex1 = eval("[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]")
    print(reducer(ex1))
