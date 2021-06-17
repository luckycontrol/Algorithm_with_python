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
    dfs_list(1)

def dfs_mat(v):
    visited[v] = True
    print(f"{v}")

    for idx, i in enumerate(adj_mat[v]):
        if i and visited[idx] is not True:
            dfs_mat(idx)

def dfs_list(v):
    visited[v] = True
    print(v)

    for i in adj_list[v]:
        if visited[i] is False:
            dfs_list(i)

if __name__ == "__main__":
    run()