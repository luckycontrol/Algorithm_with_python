# distance = 최단거리가 담겨있는 배열
# found = 선택되었던 정점

# 모든 간선의 가중치는 양수여야 한다.

# 그래프에서 정점을 선택한다.
# 해당 정점을 u 라고 할 때, distance를 weights[u]로 초기화한다.
# distance에서 최솟값을 선택한다. 이 정점이 다음으로 이동할 정점이 된다.
# 정점 u에서 다이렉트로 다른 정점으로 갈 때와 최솟값으로 선택한 정점을 거쳐서 가는 것 중
# 어느 것이 더 가중치가 적은지 비교하고, 적은 값을 distance에 넣는다.

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.weights = [
            [0 for _ in range(vertices)] for _ in range(vertices)
        ]

    def shortest_path(self, startVertex):
        found = [False] * self.V
        found[startVertex] = True

        distances = [self.weights[startVertex][i] for i in range(self.V)]

        for i in range(self.V - 1):
            u = self.__choose(startVertex, distances, found)
            found[u] = True

            for w in range(self.V):
                if found[w] is False:
                    if distances[u] + self.weights[u][w] < distances[w]:
                        distances[w] = distances[u] + self.weights[u][w]

        return distances

    def __choose(self, startVertex, distances: list, found: list) -> int:

        minVal = 1000
        minPos = -1

        for idx, distance in enumerate(distances):
            if idx != startVertex and distance != 0 and found[idx] is False:
                if distance < minVal:
                    minVal = distance
                    minPos = idx

        return minPos

    

if __name__ == "__main__":
    g = Graph(7)

    g.weights = [
        [0, 7, 1000, 1000, 3, 10, 1000],
        [7, 0, 4, 10, 2, 6, 1000],
        [1000, 4, 0, 2, 1000, 1000, 1000],
        [1000, 10, 2, 0, 11, 9, 4],
        [3, 2, 1000, 11, 0, 1000, 5],
        [10, 6, 1000, 9, 1000, 0, 1000],
        [1000, 1000, 1000, 4, 5, 1000, 0]
    ]

    result = g.shortest_path(0)
    
    print(result)