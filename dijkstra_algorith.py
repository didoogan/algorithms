graph = {
    'a': {'b': 2, 'c': 5},
    'b': {'c': 8, 'd': 7},
    'c': {'e': 4, 'd': 2},
    'd': {'f': 1},
    'e': {'f': 3, 'd': 6},
    'f': {}
}

inf = float('inf')
costs = {
    'b': 2,
    'c': 5,
    'd': inf,
    'e': inf,
    'f': inf
}
parents = {
    'b': 'a',
    'c': 'a',
    'd': None,
    'e': None,
    'f': None
}
processed = []


def find_lowest_cost_node(costs):
    lowest_cost = inf
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


if __name__ == '__main__':
    node = find_lowest_cost_node(costs)
    while node:
        cost = costs[node]
        neighbors = graph[node]
        for n in neighbors.keys():
            new_cost = cost + neighbors[n]
            if costs[n] > new_cost:
                costs[n] = new_cost
                parents[n] = node
        processed.append(node)
        node = find_lowest_cost_node(costs)
    print(costs)
    print(parents)
