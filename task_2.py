import networkx as nx
import matplotlib.pyplot as plt

# Побудова графа
G = nx.Graph()
stations = [
    "Central", "North", "South", "East", "West",
    "Park", "Museum", "Library", "Stadium", "Airport"
]
G.add_nodes_from(stations)
connections = [
    ("Central", "North"), ("Central", "South"), ("Central", "East"),
    ("Central", "West"), ("Central", "Museum"), ("Museum", "Park"),
    ("North", "Library"), ("South", "Stadium"),
    ("East", "Airport"), ("Library", "Airport")
]
G.add_edges_from(connections)

# DFS: глибина
def dfs_path(graph, start, goal, path=None, visited=None):
    if path is None:
        path = []
    if visited is None:
        visited = set()
    path = path + [start]
    visited.add(start)
    if start == goal:
        return path
    for neighbor in graph.neighbors(start):
        if neighbor not in visited:
            new_path = dfs_path(graph, neighbor, goal, path, visited)
            if new_path:
                return new_path
    return None

# BFS: ширина
def bfs_path(graph, start, goal):
    queue = [(start, [start])]
    visited = set([start])
    while queue:
        current, path = queue.pop(0)
        for neighbor in graph.neighbors(current):
            if neighbor == goal:
                return path + [goal]
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
    return None

# Шлях від 'Park' до 'Airport'
dfs_result = dfs_path(G, 'Park', 'Airport')
bfs_result = bfs_path(G, 'Park', 'Airport')

# Вивід результатів
print("🔍 DFS path from Park to Airport:", dfs_result)
print("🔍 BFS path from Park to Airport:", bfs_result)

# Візуалізація обох шляхів
def draw_path(path, title):
    plt.figure(figsize=(8, 6))
    pos = nx.spring_layout(G, seed=42)
    nx.draw(G, pos, with_labels=True, node_color='lightgray', edge_color='lightgray')
    if path:
        path_edges = list(zip(path, path[1:]))
        nx.draw_networkx_nodes(G, pos, nodelist=path, node_color='skyblue')
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='blue', width=2)
    plt.title(title)
    plt.axis('off')
    plt.show()

draw_path(dfs_result, "DFS Path from Park to Airport")
draw_path(bfs_result, "BFS Path from Park to Airport")

