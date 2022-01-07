class HasExploded(Exception):
    pass

class HasSplit(Exception):
    pass

class Node:
    def __init__(self, lst, root=None, depth=0):
        self.root = root
        self.depth = depth

        left, right = lst
        self.left = Node(left, self, depth + 1) if isinstance(left, list) else left
        self.right = Node(right, self, depth + 1) if isinstance(right, list) else right

    def __repr__(self):
        return f"[{self.left},{self.right}]"

    def __iter__(self):
        for a in ("left", "right"):
            node = getattr(self, a)
            if isinstance(node, Node):
                yield from node
            else:
                yield node, self

    @property
    def tree(self):
        current = self
        while (current := current.root).root is not None:
            pass
        return current

def find_next_non_matching_node(lst, match):
    match_found = False
    for e in lst:
        if e == match:
            match_found = True

        if e != match and match_found:
            return e[1]

def explode(tree: Node):
    if not isinstance(tree, Node):
        return False
    if tree.depth == 4:
        origin = list(tree.tree)
        left = find_next_non_matching_node(reversed(origin), (tree.left, (tree)))
        right = find_next_non_matching_node(origin, (tree.right, (tree)))

        if left is not None:
            if isinstance(left.right, int):
                left.right += tree.left
            else:
                left.left += tree.left

        if right is not None:
            if isinstance(right.left, int):
                right.left += tree.right
            else:
                right.right += tree.right

        if tree is tree.root.left:
            tree.root.left = 0
        else:
            tree.root.right = 0

        raise HasExploded

    yield from explode(tree.left)
    yield from explode(tree.right)

def split(tree: Node):
    if not isinstance(tree, Node):
        return False

    for a in ("left", "right"):
        value = getattr(tree, a)
        if isinstance(value, int) and value > 9:
            v, r = divmod(value, 2)
            new_node = Node([v, v + r], tree, depth=tree.depth + 1)
            setattr(tree, a, new_node)
            raise HasSplit

    yield from split(tree.left)
    yield from split(tree.right)

def reduce(tree: Node):
    try:
        list(explode(tree))
        return False
    except HasExploded:
        return True

def expand(tree: Node):
    try:
        list(split(tree))
        return False
    except HasSplit:
        return True

def step(tree: Node):
    b = False
    while True:
        if reduce(tree):
            print("expand:\t", tree)
            yield tree
        else:
            b = True
        if expand(tree):
            print("split:\t\t", tree)
            yield tree
        elif b:
            break

def solve(tree: Node):
    while (_ := reduce(tree)) or (_ := expand(tree)):
        pass
    return tree

def test():
    ex = [
        (eval("[[[[[9,8],1],2],3],4]"), eval("[[[[0,9],2],3],4]")),
        (eval("[7,[6,[5,[4,[3,2]]]]]"), eval("[7,[6,[5,[7,0]]]]")),
        (eval("[[6,[5,[4,[3,2]]]],1]"), eval("[[6,[5,[7,0]]],3]")),
        (
            eval("[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]"),
            eval("[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]"),
        ),
        (
            eval("[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]"),
            eval("[[3,[2,[8,0]]],[9,[5,[7,0]]]]"),
        ),
    ]
    for e, x in ex:
        node = Node(e)
        reduce(node)
        assert (eval(str(node))) == x, str(e)

    ex0 = Node(eval("[[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]"))
    assert (
        str(solve(ex0)) == "[[[[0,7],4],[[7,8],[6,0]]],[8,1]]"
    ), "[[[[0,7],4],[[7,8],[6,0]]],[8,1]]"

def test_numbers():
    numbers1 = [
        [1,1],
        [2,2],
        [3,3],
        [4,4],
        [5,5],
        [6,6]
    ]
    numbers2 = [
        [[[0, [4, 5]], [0, 0]], [[[4, 5], [2, 6]], [9, 5]]],
        [7, [[[3, 7], [4, 3]], [[6, 3], [8, 8]]]],
        [[2, [[0, 8], [3, 4]]], [[[6, 7], 1], [7, [1, 6]]]],
        [[[[2, 4], 7], [6, [0, 5]]], [[[6, 8], [2, 8]], [[2, 1], [4, 5]]]],
        [7, [5, [[3, 8], [1, 4]]]],
        [[2, [2, 2]], [8, [8, 1]]],
        [2, 9],
        [1, [[[9, 3], 9], [[9, 0], [0, 7]]]],
        [[[5, [7, 4]], 7], 1],
        [[[[4, 2], 2], 6], [8, 7]],
    ]
    for numbers in (numbers1, numbers2):
        current = Node(numbers[0])
        for number in numbers[1:]:
            print("  ", current)
            print("+ ", number)
            current = Node(eval(f"[{current}, {number}]"))
            current = solve(current)
            print("= ", current)
            print()

if __name__ == "__main__":
    e = Node(
        [
            [
                [[[7, 0], [7, 7]], [[7, 7], [7, 8]]],
                [[[7, 7], [8, 8]], [[7, 7], [8, 7]]],
            ],
            [7, [5, [[3, 8], [1, 4]]]],
        ]
    )
    s = str(solve(e))
    assert e == "[[[[7,7],[7,8]],[[9,5],[8,7]]],[[[6,8],[0,8]],[[9,9],[9,0]]]]", e
