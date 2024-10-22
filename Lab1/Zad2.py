from collections import deque
def bfsPath(graph, start, end):
    #kolekja do wierzhałków
    queue = deque([[start]])
    # zbior odwiedzonych wierszhołków
    visited = set()


    #dopóki mamy ścieżki
    while queue:
        # pobierz pierwszy wierzhołek
        path = queue.popleft()
        node = path[-1]

        if node == end:
            return path

        if node not in visited:
            for neighbor in graph.get(node,[]):
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
            visited.add(node)

    return None

graph = {
    'A' : ['B', 'C'],
    'B' : ['A', 'D', 'E'],
    'C' : ['A', 'F'],
    'D' : ['B'],
    'E' : ['B', 'F'],
    'F' : ['C', 'E']
}

print(bfsPath(graph, 'A','F'))