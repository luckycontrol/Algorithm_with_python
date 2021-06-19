from collections import deque

MAX_VERTICES = 5
visited = [False] * MAX_VERTICES

adj_mat = [
    [0, 1, 1, 1, 1],
    [1, 0, 1, 0, 0],
    [1, 1, 0, 0, 1],
    [1, 0, 0, 0, 0],
    [1, 0, 1, 0, 0]
]

adj_list = [
    [1, 2, 3, 4],
    [0, 2, 4],
    [0, 1, 4],
    [0],
    [0, 2]
]

def run():
    bfs_list(4)

def bfs_mat(v):
    queue = deque()
    queue.append(v)
    visited[v] = True
    print(v)

    while len(queue) > 0:
        v = queue.popleft()

        for idx, i in enumerate(adj_mat[v]):
            if i and visited[idx] is not True:
                visited[idx] = True
                print(idx)
                queue.append(idx)


def bfs_list(v):
    queue = deque()
    queue.append(v)
    visited[v] = True
    print(v)

    while len(queue) > 0:
        v = queue.popleft()

        for i in adj_list[v]:
            if visited[i] is not True:
                visited[i] = True
                print(i)
                queue.append(i)

if __name__ == "__main__":
    run()