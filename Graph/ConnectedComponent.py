MAX_VERTICES = 5
visited = [False] * MAX_VERTICES

adj_list = [
    [1, 2],
    [0],
    [0],
    [4],
    [3]
]

def dfs_list(v):
    visited[v] = True

    for i in adj_list[v]:
        if visited[i] is False:
            dfs_list(i)

def run():
    connected_component_result = connected_component()
    print(connected_component_result)

def connected_component():
    count = 0

    for i in range(len(adj_list)):
        if visited[i] is not True:
            count += 1
            dfs_list(i)

    return count

if __name__ == "__main__":
    run()