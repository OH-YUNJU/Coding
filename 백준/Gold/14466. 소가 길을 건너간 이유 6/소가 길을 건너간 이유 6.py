from collections import deque, defaultdict

def bfs(start, graph, visited, component_id, components):
    queue = deque([start])
    visited[start] = True
    components[start] = component_id
    while queue:
        r, c = queue.popleft()
        for nr, nc in graph[(r, c)]:
            if not visited[(nr, nc)]:
                visited[(nr, nc)] = True
                components[(nr, nc)] = component_id
                queue.append((nr, nc))

def count_isolated_pairs(n, k, roads, cows):
    # Graph representation
    graph = defaultdict(list)
    blocked = set()
    
    for r1, c1, r2, c2 in roads:
        blocked.add(((r1, c1), (r2, c2)))
        blocked.add(((r2, c2), (r1, c1)))
    
    for r in range(1, n + 1):
        for c in range(1, n + 1):
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 1 <= nr <= n and 1 <= nc <= n and ((r, c), (nr, nc)) not in blocked:
                    graph[(r, c)].append((nr, nc))
    
    # Finding connected components
    visited = defaultdict(bool)
    components = {}
    component_id = 0
    
    for r in range(1, n + 1):
        for c in range(1, n + 1):
            if not visited[(r, c)]:
                bfs((r, c), graph, visited, component_id, components)
                component_id += 1
    
    # Counting cows in each component
    cow_components = defaultdict(int)
    for cow in cows:
        cow_components[components[cow]] += 1
    
    # Calculating the number of isolated pairs
    total_cows = len(cows)
    isolated_pairs = 0
    
    for count in cow_components.values():
        isolated_pairs += count * (total_cows - count)
    
    return isolated_pairs // 2

# Input reading
n, k, r = map(int, input().strip().split())
roads = [tuple(map(int, input().strip().split())) for _ in range(r)]
cows = [tuple(map(int, input().strip().split())) for _ in range(k)]

# Calculating result
result = count_isolated_pairs(n, k, roads, cows)
print(result)
