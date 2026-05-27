# Workshop: Implement the Breadth-First Search Algorithm
from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    order = []

    while queue:
        vertex = queue.popleft()
        order.append(vertex)
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return order

def bfs_shortest_path(graph, start, goal):
    queue = deque([(start, [start])])
    visited = {start}

    while queue:
        vertex, path = queue.popleft()
        if vertex == goal:
            return path
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
    return None

graph = {"A": ["B", "C"], "B": ["A", "D", "E"], "C": ["A", "F"], "D": ["B"], "E": ["B", "F"], "F": ["C", "E"]}
print(f"BFS order: {bfs(graph, 'A')}")
print(f"Shortest path A->F: {bfs_shortest_path(graph, 'A', 'F')}")
