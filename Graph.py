import collections

# 루트는 A
graph = {
    'A': ['B'],
    'B': ['A', 'C', 'H'],
    'C': ['B', 'D'],
    'D': ['C', 'E', 'G'],
    'E': ['D', 'F'],
    'F': ['E'],
    'G': ['D'],
    'H': ['B', 'I', 'J', 'M'],
    'I': ['H'],
    'J': ['H', 'K'],
    'K': ['J', 'L'],
    'L': ['K'],
    'M': ['H']
}

def run():
    print('BFS: ', BFS(graph, 'A'))
    print('DFS: ', DFS(graph, 'A'))

def BFS(graph, root):
    # 큐를 만든다.
    # 인접 정점을 큐에 담는다.
    # 더이상 방문할 정점이없으면 큐에 있는 정점의 인접 정점을 방문한다.
    visited = []
    queue = collections.deque([root])
    
    while queue:
        n = queue.popleft()

        visited.append(n)

        for node in graph[n]:
            if node not in visited:
                queue.append(node)

    return visited


def DFS(graph, root):
    # 순환
    # 끝까지 간다.

    visited = []
    stack = [root]

    while stack:
        n = stack.pop()

        visited.append(n)
        
        for node in graph[n]:
            if node not in visited:
                stack.append(node)
    
    return visited

if __name__ == "__main__":
    run()