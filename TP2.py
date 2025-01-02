def count_components(directed_g):
    def dfs(i, c, g, visited):
        stack = [i]
        while stack:
            current = stack.pop()
            if current not in visited:
                visited.add(current)
                c.add(current + 1)
                to_extend = []
                for j in range(len(g[current])):
                    if g[current][j] == 1 and j not in visited:
                        to_extend.append(j)
                stack.extend(to_extend)

    # 💀💀💀
    undirected_g = [[1 if directed_g[i][j] or directed_g[j][i] else 0 for j in range(len(directed_g))] for i in
                    range(len(directed_g))]

    directed_visited = set()
    directed_components = []
    for i in range(len(directed_g)):
        if i not in directed_visited:
            component = set()
            dfs(i, component, directed_g, directed_visited)
            directed_components.append(component)

    undirected_visited = set()
    undirected_components = []
    for i in range(len(undirected_g)):
        if i not in undirected_visited:
            component = set()
            dfs(i, component, undirected_g, undirected_visited)
            undirected_components.append(component)

    return {"strong": directed_components, "weak": undirected_components}


if __name__ == '__main__':
    G = [
        [0, 1, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 0, 0, 0, 1],
        [0, 0, 1, 1, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 1, 1, 0, 1, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]
    result = count_components(G)
    print(result)
