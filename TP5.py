import heapq


def dijkstra(graph, src, tgt, dictionary):
    reverse_dict = {v: k for k, v in dictionary.items()}

    src_idx = reverse_dict[src]
    tgt_idx = reverse_dict[tgt]

    num_nodes = len(graph)

    distances = [float('inf')] * num_nodes
    distances[src_idx] = 0

    # priority queue to store (distance, node)
    pq = [(0, src_idx)]

    visited = [False] * num_nodes

    previous = [-1] * num_nodes

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        if current_node == tgt_idx:
            path = []
            node = tgt_idx
            while node != -1:
                path.append(dictionary[node])
                node = previous[node]
            path.reverse()
            return distances[tgt_idx], path

        if visited[current_node]:
            continue

        visited[current_node] = True

        # Iterate over all neighbors
        for neighbor, weight in enumerate(graph[current_node]):
            if weight > 0:
                distance = current_distance + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous[neighbor] = current_node
                    heapq.heappush(pq, (distance, neighbor))

    return float('inf'), []


if __name__ == '__main__':
    # GRAPH BY MR. HIEP
    g = [
        #    A  B  C  D  E  F  G  H  L  M
        [0, 4, 1, 0, 0, 0, 0, 0, 0, 0],  # A
        [4, 0, 0, 0, 0, 3, 0, 0, 0, 0],  # B
        [1, 0, 0, 8, 0, 7, 0, 0, 0, 0],  # C
        [0, 0, 8, 0, 0, 0, 0, 5, 0, 0],  # D
        [0, 0, 0, 0, 0, 1, 0, 2, 2, 0],  # E
        [0, 3, 7, 0, 1, 0, 0, 1, 0, 0],  # F
        [0, 0, 0, 0, 0, 0, 0, 3, 4, 4],  # G
        [0, 0, 0, 5, 2, 1, 3, 0, 6, 7],  # H
        [0, 0, 0, 0, 2, 6, 4, 6, 0, 1],  # L
        [0, 0, 0, 0, 0, 0, 4, 7, 1, 0],  # M
    ]

    d = {
        0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E',
        5: 'F', 6: 'G', 7: 'H', 8: 'L', 9: 'M',
    }

    s = input('Enter source node: ').upper()
    t = input('Enter target node: ').upper()

    shortest_distance, shortest_path = dijkstra(g, s, t, d)

    if shortest_distance != float('inf'):
        print(f"The shortest distance from {s} to {t} is {shortest_distance}")
        print(f"The shortest path is: {' -> '.join(shortest_path)}")
    else:
        print(f"There is no path from {s} to {t}")
