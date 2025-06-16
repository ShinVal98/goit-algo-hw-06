import networkx as nx
import matplotlib.pyplot as plt

# Створюємо граф з вагами
G = nx.Graph()

# Додаємо вузли та ребра з вагами (наприклад, транспортна мережа міста)
edges = [
    ('A', 'B', 4),
    ('A', 'C', 2),
    ('B', 'C', 1),
    ('B', 'D', 5),
    ('C', 'D', 8),
    ('C', 'E', 10),
    ('D', 'E', 2),
    ('D', 'Z', 6),
    ('E', 'Z', 3)
]

for u, v, w in edges:
    G.add_edge(u, v, weight=w)

# Візуалізація графа
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000, font_size=14)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.title("Граф із вагами для алгоритму Дейкстри")
plt.show()

# Алгоритм Дейкстри для знаходження найкоротшого шляху
start_node = 'A'
lengths, paths = nx.single_source_dijkstra(G, source=start_node)

print(f"Найкоротші шляхи від вузла '{start_node}':")
for target in G.nodes():
    if target == start_node:
        continue
    print(f"  До {target}: шлях {paths[target]}, довжина = {lengths[target]}")
