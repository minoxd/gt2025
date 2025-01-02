def path_existence(g: dict, s:int, t:int) -> bool:
    def extract_edges(g: dict) -> list[tuple[int, int]]:
        edges = []
        for key in g.keys():
            for value in g[key]:
                edges.append((key, value))
        return edges

    visited = []
    not_visited = list(g.keys())
    edges = extract_edges(g)

    visited.append(s)
    not_visited.remove(s)
    def no_more_vertice(nv, checkpoint_nv) -> bool:
        if nv==checkpoint_nv:
            return True
        return False
    checkpoint_not_visited = []
    while not no_more_vertice(not_visited, checkpoint_not_visited):
        checkpoint_not_visited = not_visited
        for u in visited:
            markable = [edge[1] for edge in edges if edge[0]==u]
            for m in markable:
                if m in visited:
                    continue
                visited.append(m)
                not_visited.remove(m)
    if t in visited:
        return True
    return False

if __name__ == '__main__':
    tp1 = path_existence({
        1: [2],
        2: [1, 5],
        3: [6],
        4: [6, 7],
        5: [2],
        6: [3, 4, 7],
        7: [4, 6],
    }, 2, 6)
    print(tp1)