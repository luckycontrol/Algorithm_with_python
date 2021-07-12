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