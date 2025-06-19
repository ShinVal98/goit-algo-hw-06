import networkx as nx
import matplotlib.pyplot as plt

# Створюємо граф (як приклад, я взяла транспортну мережу метро)
G = nx.Graph()

# Додаємо вузли (станції метро)
stations = [
    "Central", "North", "South", "East", "West",
    "Park", "Museum", "Library", "Stadium", "Airport"
]
G.add_nodes_from(stations)

# Додаємо ребра (лінії метро між станціями)
connections = [
    ("Central", "North"),
    ("Central", "South"),
    ("Central", "East"),
    ("Central", "West"),
    ("Central", "Museum"),
    ("Museum", "Park"),
    ("North", "Library"),
    ("South", "Stadium"),
    ("East", "Airport"),
    ("Library", "Airport")
]
G.add_edges_from(connections)

# Візуалізуємо граф
plt.figure(figsize=(10, 7))
pos = nx.spring_layout(G, seed=42)
nx.draw_networkx_nodes(G, pos, node_color='lightblue', node_size=900)
nx.draw_networkx_edges(G, pos, width=2)
nx.draw_networkx_labels(G, pos, font_size=11, font_weight='bold')
plt.title("🚇 Metro Transport Network Graph", fontsize=14)
plt.axis('off')
plt.show()

# Аналіз характеристик графа
print("📊 Аналіз графа:")
print(f"- Кількість вузлів (станцій): {G.number_of_nodes()}")
print(f"- Кількість ребер (ліній метро): {G.number_of_edges()}")
print(f"- Ступені вузлів (кількість з'єднань):")
for node, degree in G.degree():
    print(f"  • {node}: {degree}")
