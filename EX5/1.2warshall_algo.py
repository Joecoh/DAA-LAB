def floyd_warshall(graph):
    n = len(graph)
    
    # Initialize the distance matrix
    dist = [row[:] for row in graph]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist

# Example usage:
inf = float('inf')
graph = [
    [0, 3, inf, 5],
    [2, 0, inf, 4],
    [inf, 1, 0, inf],
    [inf, inf, 2, 0]
]

shortest_paths = floyd_warshall(graph)
print("Shortest Paths:")
for row in shortest_paths:
    print(row)
