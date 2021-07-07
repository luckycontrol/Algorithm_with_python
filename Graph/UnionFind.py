def run():
    pass

class Union_Find:
    def __init__(self, vertices):
        self.parent = [-1] * vertices
        self.num = [1] * vertices

    def set_union(self, x, y):
        if self.num[x] > self.num[y]:
            self.parent[y] = x
            self.num[x] += self.num[y]

        else:
            self.parent[x] = y
            self.num[y] += self.num[x]

    def set_find(self, vertex):
        if self.parent[vertex] == -1: return vertex
        if self.parent[vertex] != -1: return self.set_find(self.parent[vertex])

if __name__ == "__main__":
    run()