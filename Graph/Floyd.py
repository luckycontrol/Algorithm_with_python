class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.weights = [
            [0 for _ in range(vertices)] for _ in range(vertices)
        ]

    def shortest_path(self):
        A = self.weights

        for k in range(self.V):
            for i in range(self.V):
                for j in range(self.V):
                    if self.weights[i][k] + self.weights[k][j] < A[i][j]:
                        A[i][j] = self.weights[i][k] + self.weights[k][j]

        return A

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

    result = g.shortest_path()
    print(result)

