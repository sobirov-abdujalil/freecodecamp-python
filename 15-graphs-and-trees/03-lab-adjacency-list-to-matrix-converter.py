# Lab: Build an Adjacency List to Matrix Converter
def adjacency_list_to_matrix(adj_list):
    nodes = sorted(adj_list.keys())
    node_index = {node: i for i, node in enumerate(nodes)}
    n = len(nodes)
    matrix = [[0] * n for _ in range(n)]

    for node, neighbors in adj_list.items():
        i = node_index[node]
        for neighbor in neighbors:
            j = node_index[neighbor]
            matrix[i][j] = 1
    return matrix, nodes

def matrix_to_adjacency_list(matrix, nodes):
    adj_list = {node: [] for node in nodes}
    for i, node in enumerate(nodes):
        for j, val in enumerate(matrix[i]):
            if val:
                adj_list[node].append(nodes[j])
    return adj_list

adj = {"A": ["B", "C"], "B": ["C"], "C": ["A"]}
mat, nodes = adjacency_list_to_matrix(adj)
print("Matrix:", mat)
print("Nodes:", nodes)
