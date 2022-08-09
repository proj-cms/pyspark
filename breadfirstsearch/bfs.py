# Implementing BFS
import collections


def bfs(graph, root):
    visited = set()
    queue = collections.deque([root])

    while queue:
        vertex = queue.popleft()  # Dequeue
        visited.add(vertex)  # Add to visited
        for i in graph[vertex]:  # Traverse the list at graph[vertex]
            if i not in visited:  # Check if visited
                queue.append(i)  # Enqueue
    print(visited)  # Final Result


if __name__ == "__main__":
    # Dictionary representation of Graph
    graph = {
        0: [1, 2, 3],
        1: [0, 2],
        2: [0, 1, 4],
        3: [0],
        4: [2]
    }
    bfs(graph, 0)
