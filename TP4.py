import sys


class Graph:
    def __init__(self, graph):
        self.V = len(graph)
        self.graph = graph


    # Prim's Algorithm
    def prim_mst(self, start_node):
        key = [sys.maxsize] * self.V
        parent = [None] * self.V
        key[start_node] = 0
        mst_set = [False] * self.V
        parent[start_node] = -1

        for _ in range(self.V):
            u = self.min_key(key, mst_set)
            mst_set[u] = True

            for v in range(self.V):
                if self.graph[u][v] > 0 and not mst_set[v] and key[v] > self.graph[u][v]:
                    key[v] = self.graph[u][v]
                    parent[v] = u

        print("Edge \tWeight")
        for i in range(1, self.V + 1):
            if parent[i - 1] + 1 == 0:
                continue
            print(f"{i} - {parent[i - 1] + 1}\t{self.graph[i - 1][parent[i - 1]]}")

    def min_key(self, key, mst_set):
        min_val = sys.maxsize
        min_index = -1
        for v in range(self.V):
            if key[v] < min_val and not mst_set[v]:
                min_val = key[v]
                min_index = v
        return min_index

    # Kruskal's Algorithm
    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):
        x_root = self.find(parent, x)
        y_root = self.find(parent, y)

        if rank[x_root] < rank[y_root]:
            parent[x_root] = y_root
        elif rank[x_root] > rank[y_root]:
            parent[y_root] = x_root
        else:
            parent[y_root] = x_root
            rank[x_root] += 1

    def kruskal_mst(self):
        result = []
        i, e = 0, 0

        edges = []
        for u in range(self.V):
            for v in range(u + 1, self.V):
                if self.graph[u][v] > 0:
                    edges.append((u, v, self.graph[u][v]))
        edges = sorted(edges, key=lambda item: item[2])

        parent = []
        rank = []

        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        while e < self.V - 1:
            u, v, w = edges[i]
            i += 1
            x = self.find(parent, u)
            y = self.find(parent, v)

            # if not circle, add
            if x != y:
                e += 1
                result.append((u, v, w))
                self.union(parent, rank, x, y)

        # Print the MST
        print("Edge \tWeight")
        for u, v, w in result:
            print(f"{u + 1} - {v + 1}\t{w}")


def main():
    adj_matrix = [
        [0, 4, 0, 0,  1, 0,  2, 0, 0],
        [4, 0, 7, 0,  0, 5,  0, 0, 0],
        [0, 7, 0, 1,  0, 8,  0, 0, 0],
        [0, 0, 1, 0,  0, 6,  4, 3, 0],
        [1, 0, 0, 0,  0, 9, 10, 0, 0],
        [0, 5, 8, 6,  9, 0,  0, 0, 2],
        [2, 0, 0, 4, 10, 0,  2, 0, 8],
        [0, 0, 0, 3,  0, 0,  0, 0, 1],
        [0, 0, 0, 0,  0, 2,  8, 1, 0],
    ]
    g = Graph(adj_matrix)

    start_node = int(input("Enter the LABEL of starting node (not the 0-based one) for Prim's algorithm: "))
    if start_node < 1 or start_node > len(adj_matrix):
        print("Invalid starting node! Please enter a valid node.")
        return

    print("\nPrim's MST (starting node: 3, ordered by u if edges are {u, v}):")
    g.prim_mst(start_node - 1)

    print("\nKruskal's MST:")
    g.kruskal_mst()


if __name__ == "__main__":
    main()
