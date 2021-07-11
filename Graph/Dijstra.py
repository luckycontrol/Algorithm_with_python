class Dijstra:
    def __init__(self, vertices):
        self.V = vertices
        self.distances = [0] * vertices
        self.found = [False] * vertices
        self.weight = [
            [0 for _ in range(vertices)] for _ in range(vertices)
        ]

    def shortest_path(self, start):
        self.distances = [self.weight[start][i] for i in range(self.V)]
        self.found[start] = True

        for _ in range(self.V - 1):
            u = self.choose(start, self.distances, self.found)
            self.found[u] = True
            for w in range(self.V):
                if not self.found[w]:
                    if self.distances[u] + self.weight[u][w] < self.distances[w]:
                        self.distances[w] = self.distances[u] + self.weight[u][w]


    def choose(self, startVertex: int, distances: list, found: list) -> int:
        minValue = 1000
        minPos = -1

        for i in range(self.V):
            if i != startVertex:
                if distances[i] < minValue and found[i] == False:
                    minValue = distances[i]
                    minPos = i

        return minPos


g = Dijstra(7)

g.weight = [
    [0, 7, 1000, 1000, 3, 10, 1000],
    [7, 0, 4, 10, 2, 6, 1000],
    [1000, 4, 0, 2, 1000, 1000, 1000],
    [1000, 10, 2, 0, 11, 9, 4],
    [3, 2, 1000, 11, 0, 1000, 5],
    [10, 6, 1000, 9, 1000, 0, 1000],
    [1000, 1000, 1000, 4, 5, 1000, 0]
]

g.shortest_path(0)
print(g.distances)