"""Friends"""
# from collections import defaultdict


# n = int(input())
# edges = []
# for _ in range(n):
#     mew = [int(x) for x in input().split()]
#     edges.append(mew)

# graph = defaultdict(list)

# for edge in edges:
#     a, b = edge[0], edge[1]
#     graph[a].append(b)
#     graph[b].append(a)


# def has_triangle(graph):
#     for u in graph:
#         for v in graph[u]:
#             for w in graph[v]:
#                 if w in graph[u]:
#                     return "YES"
#     return "NO"


# result = has_triangle(graph)
# print(result)


"""Circles"""
# from collections import defaultdict


# n = int(input())
# edges = []
# for _ in range(n):
#     mew = [int(x) for x in input().split()]
#     edges.append(mew)

# graph = defaultdict(list)

# for edge in edges:
#     a, b = edge[0], edge[1]
#     flag = True
#     for i in graph:
#         if a in graph[i]:
#             graph[i].append(b)
#             flag = False
#     if flag:
#         graph[a].append(b)
# print(len(graph))


# """Ways"""

# n = int(input())
# matrix = [[int(x) for x in input().split()] for _ in range(n)]
# start = int(input()) - 1

# inf = 1e9
# visited = [False] * n
# dist = [inf] * n
# dist[start] = 0


# def gofrom():
#     index = 0
#     distmin = inf
#     for i in range(n):
#         if dist[i] < distmin and (visited[i] == False):
#             distmin = dist[i]
#             index = i
#     return index

# while False in visited:
#     toStart = gofrom()
#     for v in range(n):
#         if matrix[toStart][v] != 0 and (not visited[v]):
#             dist[v] = min(dist[v], dist[toStart] + matrix[toStart][v])
#     visited[toStart] = True

# print(dist)



# """Пересадки"""
# from collections import defaultdict, deque

# n = int(input())
# edges = [[int(x) for x in input().split()] for _ in range(n)]
# start_station, end_station = map(int, input().split())


# graph = defaultdict(list)
# for edge in edges:
#     a, b = edge
#     graph[a].append(b)
#     graph[b].append(a)


# def bfs_shortest_path(graph, start, end):
#     if start not in graph or end not in graph:
#         return None
#     queue = deque([(start, [start])])
#     while queue:
#         vertex, path = queue.popleft()
#         for next_vertex in graph[vertex]:
#             if next_vertex == end:
#                 return path + [end]
#             if next_vertex not in path:
#                 queue.append((next_vertex, path + [next_vertex]))
#     return None

# # Находим кратчайший путь между начальной и конечной станциями
# shortest_path = bfs_shortest_path(graph, start_station, end_station)
# if shortest_path is not None:
#     import math
#     print(int(math.ceil(len(shortest_path) / 2)))
# else:
#     print("No path found")


# import collections
# def bfs(graph, root): 
#     visited, queue = set(), collections.deque([root])
#     visited.add(root)
#     while queue: 
#         vertex = queue.popleft()
#         for neighbour in graph[vertex]: 
#             if neighbour not in visited: 
#                 visited.add(neighbour) 
#                 queue.append(neighbour) 
    
# if __name__ == '__main__':
#     graph = {0: [1, 2], 1: [2], 2: [3], 3: [1,2]} 
#     bfs(graph, 0)


"""Перекрестки"""

n = int(input())
edges = [
    [int(x) for x in input().split()] for _ in range(n)
]
start_crossroad, end_crossroad = map(int, input().split())

graph = {}
for edge in edges:
    a, b, weight = edge
    if a not in graph:
        graph[a] = {}
    if b not in graph:
        graph[b] = {}
    graph[a][b] = weight
    graph[b][a] = weight

def dijkstra_with_length(graph, start, end):
    costs = {node: float('inf') for node in graph}
    costs[start] = 0
    parents = {node: None for node in graph}
    visited = []

    while True:
        min_node = None
        for node in graph:
            if node not in visited and (min_node is None or costs[node] < costs[min_node]):
                min_node = node

        if min_node is None:
            break

        for neighbor in graph[min_node]:
            new_cost = costs[min_node] + graph[min_node][neighbor]
            if new_cost < costs[neighbor]:
                costs[neighbor] = new_cost
                parents[neighbor] = min_node

        visited.append(min_node)

    path = []
    current = end
    while current is not None:
        path.insert(0, current)
        current = parents[current]

    length = costs[end]
    return path, length


fastest_path, path_length = dijkstra_with_length(graph, start_crossroad, end_crossroad)
if not fastest_path:
    print("No path found")
else:
    print(path_length)