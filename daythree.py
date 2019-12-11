from operator import sub, add


def extend_path(points, direction, n_steps):
    op = sub if direction in ("L", "D",) else add
    points.extend(
        [
            (points[-1][0], op(points[-1][1], i))
            if direction in ("D", "U", ) else
            (op(points[-1][0], i), points[-1][1])
            for i in range(1, n_steps + 1)
        ]
    )


def compute_distance(wire1, wire2, return_steps=False):
    starting_point = (0, 0)
    wire1_points = [starting_point]
    wire2_points = [starting_point]
    for point in wire1:
        extend_path(wire1_points, point[0], int(point[1:]))

    for point in wire2:
        extend_path(wire2_points, point[0], int(point[1:]))

    intersections = set(wire1_points[1:]).intersection(set(wire2_points[1:]))
    if return_steps:
        return min(
            wire1_points.index(i) + wire2_points.index(i)
            for i in intersections
        )

    intersections = list(map(lambda x: (abs(x[0]), abs(x[1]),), intersections))
    return min(filter(None, map(sum, intersections)))


if __name__ == "__main__":
    assert compute_distance(
        ["R8", "U5", "L5", "D3"],
        ["U7", "R6", "D4", "L4"]
    ) == 6

    assert compute_distance(
        ["R8", "U5", "L5", "D3"],
        ["U7", "R6", "D4", "L4"],
        return_steps=True
    ) == 30
    with open("inputdaythree.txt") as f:
        wires = [
            [i.strip() for i in x.split(",")] for x in f.readlines()
        ]

    assert compute_distance(*wires) == 1983
    assert compute_distance(*wires, return_steps=True) == 107754 
