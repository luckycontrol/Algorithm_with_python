class Element:
    def __init__(self, key, x, y):
        self.key = key
        self.x = x
        self.y = y

class Kruskal:
    def __init__(self):
        self.elements = []

    def insertEdge(self, x, y, key):
        element = {
            "key": key,
            "s1": x,
            "s2": y
        }

        self.elements.append(element)

    def run(self, elements) -> list:
        union_find = UnionFind(7)
        result = []

        for edge in elements:
            isCycle = union_find.isCycle(edge["s1"], edge["s2"])
            if isCycle: continue

            result.append(edge)
            union_find.set_union(edge["s1"], edge["s2"])

        return result

    # 정렬 - 퀵정렬
    def sort(self) -> list:
        return self.__quickSort(self.elements)

    # 퀵정렬
    def __quickSort(self, arr) -> list:
        if len(arr) <= 1: return arr
        pivot = arr[0]

        left = list(filter(lambda element: element["key"] < pivot["key"], arr))
        right = list(filter(lambda element: element["key"] > pivot["key"], arr))

        newLeft = self.__quickSort(left)
        newRight = self.__quickSort(right)

        return newLeft + [pivot] + newRight

class UnionFind:
    def __init__(self, n):
        self.parent = [-1] * n
        self.num = [1] * n

    def set_find(self, vertex):
        if self.parent[vertex] == -1: return vertex
        if self.parent[vertex] != -1: return self.set_find(self.parent[vertex])

    def set_union(self, x, y):
        if self.num[x] < self.num[y]:
            self.parent[x] = y
            self.num[y] += self.num[x]

        else:
            self.parent[y] = x
            self.num[x] += self.num[y]

    def isCycle(self, x, y):
        x_result = self.set_find(x)
        y_result = self.set_find(y)

        if x_result == y_result: return True
        else: return False

k = Kruskal()
k.insertEdge(0, 1, 29)
k.insertEdge(1, 2, 16)
k.insertEdge(2, 3, 12)
k.insertEdge(3, 4, 22)
k.insertEdge(4, 5, 27)
k.insertEdge(5, 0, 10)
k.insertEdge(1, 6, 15)
k.insertEdge(4, 6, 25)
k.insertEdge(3, 6, 18)

sortedElements = k.sort()
kruskal_result = k.run(sortedElements)

print(kruskal_result)