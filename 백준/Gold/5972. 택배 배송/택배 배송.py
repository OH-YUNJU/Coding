import heapq

def dijkstra(graph, start, end):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    queue = [(0, start)]

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if current_distance > distances[current_node]:
            continue

        for adjacent, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[adjacent]:
                distances[adjacent] = distance
                heapq.heappush(queue, (distance, adjacent))

    return distances[end]

N, M = map(int, input().split())
graph = {i: {} for i in range(1, N+1)}

for _ in range(M):
    A, B, C = map(int, input().split())
    if B in graph[A]:
        graph[A][B] = min(graph[A][B], C)
        graph[B][A] = min(graph[B][A], C)
    else:
        graph[A][B] = C
        graph[B][A] = C

min_food = dijkstra(graph, 1, N)
print(min_food)
