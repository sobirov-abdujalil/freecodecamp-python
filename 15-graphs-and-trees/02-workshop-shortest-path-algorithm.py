# Workshop: Implement the Shortest Path Algorithm
import heapq

def dijkstra(graph, start):
    distances = {node: float("inf") for node in graph}
    distances[start] = 0
    pq = [(0, start)]

    while pq:
        current_dist, current = heapq.heappop(pq)
        if current_dist > distances[current]:
            continue
        for neighbor, weight in graph[current].items():
            distance = current_dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    return distances

graph = {
    "A": {"B": 4, "C": 2},
    "B": {"A": 4, "C": 1, "D": 5},
    "C": {"A": 2, "B": 1, "D": 8},
    "D": {"B": 5, "C": 8},
}

result = dijkstra(graph, "A")
print(f"Shortest paths from A: {result}")
