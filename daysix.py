def make_reverse_graph(edges):
    'Note: Each target edge can only have one source edge'
    reverse_graph = dict()
    for source, target in edges:
        reverse_graph[target] = source
    return reverse_graph


def count_orbits(edges):
    reverse_graph = make_reverse_graph(edges)
    counts = 0
    for node, current_node in reverse_graph.items():
        while current_node:
            counts += 1
            current_node = reverse_graph.get(current_node)
    return counts


def compute_shortest_number_of_orbital_transfers(edges, node1="YOU", node2="SAN"):
    reverse_graph = make_reverse_graph(edges)
    paths = []
    for node in (node1, node2, ):
        path = []
        current_node = reverse_graph.get(node)
        while current_node:
            path.append(current_node)
            current_node = reverse_graph.get(current_node)
        paths.append(path)

    common_nodes = set(paths[0]).intersection(set(paths[1]))
    return min(
        (paths[0].index(node) + paths[1].index(node) for node in common_nodes)
    )


if __name__ == "__main__":
    test_edges = [
        ("COM", "B"),
        ("B", "C"),
        ("C", "D"),
        ("D", "E"),
        ("E", "F"),
        ("B", "G"),
        ("G", "H"),
        ("D", "I"),
        ("E", "J"),
        ("J", "K"),
        ("K", "L"),
    ]
    assert count_orbits(test_edges) == 42
    with open("inputdaysix.txt", 'r') as f:
        edges = [x.strip().split(")") for x in f.readlines()]
        assert count_orbits(edges) == 344238

    test_edges = [
        ("COM", "B"),
        ("B", "C"),
        ("C", "D"),
        ("D", "E"),
        ("E", "F"),
        ("B", "G"),
        ("G", "H"),
        ("D", "I"),
        ("E", "J"),
        ("J", "K"),
        ("K", "L"),
        ("K", "YOU"),
        ("I", "SAN")
    ]

    assert compute_shortest_number_of_orbital_transfers(
        test_edges
    ) == 4

    assert compute_shortest_number_of_orbital_transfers(
            edges
        ) == 436
