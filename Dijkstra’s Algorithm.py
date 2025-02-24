import heapq

def dijkstra(graph, start):
    # Initialize distances with infinity
    distances = {node: float('inf') for node in graph}
    distances[start] = 0  # Distance to the start node is 0

    # Priority queue (min-heap)
    pq = [(0, start)]  # (distance, node)

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        # If we already found a shorter path before, ignore this
        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # If found a shorter path to neighbor, update it
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances

graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

start_node = 'A'
shortest_paths = dijkstra(graph, start_node)
print(shortest_paths)
