import networkx as nx
import matplotlib.pyplot as plt

# Створення графа G
G = nx.Graph()

# Додаємо вершини (наприклад, зупинки транспорту)
nodes = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
G.add_nodes_from(nodes)

# Додаємо ребра (наприклад, дороги або маршрути)
edges = [
    ('A', 'B'), ('A', 'C'),
    ('B', 'D'),
    ('C', 'E'),
    ('D', 'E'),
    ('E', 'F'),
    ('F', 'G'), ('F', 'H')
]
G.add_edges_from(edges)

# Візуалізація графа
plt.figure(figsize=(8, 6))
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=1000, font_size=14)
plt.title("Модель транспортної мережі")
plt.show()

# DFS (пошук в глибину)
dfs_path = list(nx.dfs_preorder_nodes(G, source='A'))
print("DFS path:", dfs_path)

# BFS (пошук в ширину)
bfs_path = list(nx.bfs_tree(G, source='A').nodes())
print("BFS path:", bfs_path)

# Пояснення
print("\nПояснення:")
print("DFS йде якнайглибше по одному напрямку, перш ніж повернутись і піти іншим шляхом.")
print("BFS досліджує всі сусідні вершини перед тим, як перейти на наступний рівень глибини.")
