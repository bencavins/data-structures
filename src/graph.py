adj_mat = [
    [0, 1, 0, 0, 0],
    [1, 0, 1, 1, 1],
    [0, 1, 0, 1, 0],
    [0, 1, 1, 0, 0],
    [0, 1, 0, 0, 0],
]

adj_list = [
    [1],
    [1, 3, 4],
    [1, 3],
    [1, 2],
    [1]
]

def dfs_adj_mat(m):
    seen = set()
    def traverse(node):
        seen.add(node)
        print(node)
        for adj_node, is_edge in enumerate(m[node]):
            if is_edge and adj_node not in seen:
                traverse(adj_node)
    traverse(0)
