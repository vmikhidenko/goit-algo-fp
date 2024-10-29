import heapq

# Функція для алгоритму Дейкстри
def dijkstra(graph, start):
    # Ініціалізація відстаней і батьківських вузлів
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    priority_queue = [(0, start)]
    
    while priority_queue:
        # Вибираємо вершину з найменшою відстанню
        current_distance, current_vertex = heapq.heappop(priority_queue)
        
        # Пропускаємо вершини, які вже мають мінімальну відстань
        if current_distance > distances[current_vertex]:
            continue
        
        # Оновлюємо відстань до сусідів
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            
            # Якщо знайшли коротший шлях, оновлюємо його
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances

# Приклад графу (зважений)
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

# Викликаємо функцію для знаходження найкоротших шляхів від вершини 'A'
start_vertex = 'A'
shortest_paths = dijkstra(graph, start_vertex)

# Виводимо результати
print(f"Найкоротші шляхи від вершини {start_vertex}:")
for vertex, distance in shortest_paths.items():
    print(f"Відстань до {vertex}: {distance}")
