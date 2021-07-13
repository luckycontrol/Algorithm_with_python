from collections import deque

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.adj_mat = [
            [0 for _ in range(self.V)] for _ in range(self.V)
        ]

    # 위상 정렬
    def topological_sort(self):
        stack = deque()
        answer = []
        selected = []

        min_degrees = self.return_min_degrees(selected=selected)
        for min_degree in min_degrees:
            stack.append(min_degree)
            selected.append(min_degree)

                

        pass

    # 차수 계산
    def cal_degrees(self):
        degrees = []

        for i in range(self.V):
            result = 0
            for j in range(self.V):
                result += self.adj_mat[j][i]

            degrees.append(result)

        return degrees

    # 차수 중 최솟값 반환
    def return_min_degrees(self, selected: list):
        degrees = self.cal_degrees()
        min_degrees = []

        for idx, degree in enumerate(degrees):
            if degree == 0 and idx not in selected: min_degrees.append(idx)

        return min_degrees

g = Graph(6)

g.adj_mat = [
    [0, 0, 1, 1, 0, 0],
    [0, 0, 0, 1, 1, 0],
    [0, 0, 0, 1, 0, 1],
    [0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0]
]

