# 방문한 정점을 담은 배열
# 모든 정점을 담은 배열

# 1. 시작 정점을 방문한 정점 배열에 담는다.
# 2. 시작 정점과 연결된 점들을 우선 순위 큐 or 힙 에 담는다.
# 3. 가장 가중치가 작은 간선의 점을 빼내서 사이클이 발생하는지 확인한다.
# 4. 사이클이 없으면 해당 간선을 선택. 발생하면 다른 점을 선택한다.
# 5. 위 과정을 모든 정점을 방문할 때 까지 반복한다.

class Graph:
    def __init__(self, vertices):
        self.V = vertices

        self.graph = [
            [0 for _ in range(vertices)] for _ in range(vertices)
        ]

        self.selected = []

        self.heap = [{}, ]

    def prim(self, start):

        print(f"{start} -> ")
        self.selected.append(start)

        while len(self.selected) < self.V:
            # 정점들과 인접한 것들 중 사이클이 되지 않고 가장 작은 점을 찾는다.
            min_vertex = self.findMinVertex()
            print(f"{min_vertex['sv']} - {min_vertex['ev']} : {min_vertex['value']} ->")
            self.selected.append(min_vertex["ev"])

    def findMinVertex(self) -> dict:
        for selectedVertex in self.selected:
            for vertex, value in enumerate(self.graph[selectedVertex]):
                if value > 0 and vertex not in self.selected:
                    self.insertHeap(startVertex=selectedVertex, endVertex=vertex, value=value)

        min_vertex = self.heap[1]
        self.heap = [{}, ]

        return min_vertex

    def insertHeap(self, startVertex, endVertex, value):
        element = {
            "sv": startVertex,
            "ev": endVertex,
            "v": value
        }

        self.heap.append(element)
        idx = len(self.heap)

        while idx > 1:
            parent = idx // 2
            if self.heap[parent] > self.heap[idx]:
                self.heap[parent], self.heap[idx] = self.heap[idx], self.heap[parent]
                idx = idx // 2

            else: break


g = Graph(vertices=7)
g.graph = [
    [0, 29, 0, 0, 0, 10, 0],
    [29, 0, 16, 0, 0, 0, 15],
    [0, 16, 0, 12, 0, 0, 0],
    [0, 0, 12, 0, 22, 0, 18],
    [0, 0, 0, 22, 0, 27, 25],
    [10, 0, 0, 0, 27, 0, 0],
    [0, 15, 0, 18, 25, 0, 0]
]

g.prim(0)