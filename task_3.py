import networkx as nx
import matplotlib.pyplot as plt

# Створення графа з вагами
G = nx.Graph()

# Вузли (станції)
stations = [
    "Central", "North", "South", "East", "West",
    "Park", "Museum", "Library", "Stadium", "Airport"
]
G.add_nodes_from(stations)

# Ребра з вагами (наприклад: відстань у хвилинах)
weighted_connections = [
    ("Central", "North", 5),
    ("Central", "South", 4),
    ("Central", "East", 6),
    ("Central", "West", 7),
    ("Central", "Museum", 3),
    ("Museum", "Park", 4),
    ("North", "Library", 6),
    ("South", "Stadium", 8),
    ("East", "Airport", 5),
    ("Library", "Airport", 7)
]

G.add_weighted_edges_from(weighted_connections)

# Візуалізація графа з вагами
pos = nx.spring_layout(G, seed=42)
edge_labels = nx.get_edge_attributes(G, 'weight')

plt.figure(figsize=(10, 7))
nx.draw(G, pos, with_labels=True, node_color='lightgreen', node_size=800)
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
plt.title("Metro Graph with Weights (Minutes Between Stations)")
plt.axis('off')
plt.show()

# Використання алгоритму Дейкстри
source = "Park"
target = "Stadium"
shortest_path = nx.dijkstra_path(G, source, target)
shortest_distance = nx.dijkstra_path_length(G, source, target)

print(f"🚇 Найкоротший шлях від {source} до {target}:")
print(" → ".join(shortest_path))
print(f"Загальна вага (час): {shortest_distance} хв.")

