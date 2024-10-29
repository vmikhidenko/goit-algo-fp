import networkx as nx
import matplotlib.pyplot as plt
from matplotlib import colors as mcolors
from collections import deque

# Визначення класу вузла бінарного дерева
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Функція для вставки нового вузла в бінарне дерево
def insert(root, key):
    if root is None:
        return TreeNode(key)
    else:
        queue = deque()
        queue.append(root)
        while queue:
            temp = queue.popleft()
            if temp.left is None:
                temp.left = TreeNode(key)
                break
            else:
                queue.append(temp.left)
            if temp.right is None:
                temp.right = TreeNode(key)
                break
            else:
                queue.append(temp.right)
    return root

# Функція для побудови графу з бінарного дерева
def build_graph(root):
    G = nx.Graph()
    queue = deque()
    queue.append(root)
    while queue:
        node = queue.popleft()
        if node.left:
            G.add_edge(node.value, node.left.value)
            queue.append(node.left)
        if node.right:
            G.add_edge(node.value, node.right.value)
            queue.append(node.right)
    return G

# Функція для обходу в глибину з візуалізацією
def dfs_visualize(root):
    G = build_graph(root)
    stack = []
    visited = set()
    order = []
    color_map = {}

    stack.append(root)
    count = 0

    while stack:
        node = stack.pop()
        if node.value not in visited:
            visited.add(node.value)
            order.append(node.value)
            # Генеруємо колір
            color = mcolors.rgb_to_hsv([count/15, 0.5, 0.8])
            color_map[node.value] = (count/15, 0.5, 0.8)
            count += 1
            # Додаємо сусідів в стек
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

    # Відображаємо граф
    colors_list = [mcolors.hsv_to_rgb(color_map.get(node, (0, 0, 0))) for node in G.nodes()]
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color=colors_list)
    plt.title("Обхід в глибину")
    plt.show()

# Функція для обходу в ширину з візуалізацією
def bfs_visualize(root):
    G = build_graph(root)
    queue = deque()
    visited = set()
    order = []
    color_map = {}

    queue.append(root)
    count = 0

    while queue:
        node = queue.popleft()
        if node.value not in visited:
            visited.add(node.value)
            order.append(node.value)
            # Генеруємо колір
            color = mcolors.rgb_to_hsv([count/15, 0.5, 0.8])
            color_map[node.value] = (count/15, 0.5, 0.8)
            count += 1
            # Додаємо сусідів в чергу
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    # Відображаємо граф
    colors_list = [mcolors.hsv_to_rgb(color_map.get(node, (0, 0, 0))) for node in G.nodes()]
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color=colors_list)
    plt.title("Обхід в ширину")
    plt.show()

# Приклад використання функцій
if __name__ == "__main__":
    # Створюємо бінарне дерево
    root = None
    elements = [1, 2, 3, 4, 5, 6, 7]
    for elem in elements:
        root = insert(root, elem)

    # Візуалізація обходу в глибину
    dfs_visualize(root)

    # Візуалізація обходу в ширину
    bfs_visualize(root)
