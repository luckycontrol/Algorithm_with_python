from enum import Enum

class Heap:
    def __init__(self):
        self.arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.heap_size = 1

    def insert(self, x):
        idx = self.heap_size
        self.heap_size += 1

        while idx != 1 and x > self.arr[idx // 2]:
            self.arr[idx] = self.arr[idx // 2]
            idx //= 2
        
        self.arr[idx] = x

    def delete(self):
        item = self.arr[1]
        tmp = self.arr[self.heap_size - 1]
        self.arr[self.heap_size - 1] = 0
        self.heap_size -= 1

        parent = 1
        child = 2

        while child <= self.heap_size:
            if child < self.heap_size and self.arr[child] > self.arr[child + 1]:
                child  += 1

            if self.arr[parent] > self.arr[child]: break
            self.arr[parent] = self.arr[child]
            parent = child
            child *= 2

        self.arr[parent] = tmp
        return item

def run():
    heap = Heap()
    heap.insert(5)
    heap.insert(7)
    heap.insert(3)
    heap.insert(6)
    heap.insert(12)
    print(heap.arr)

    heap.delete()
    print(heap.arr)
    heap.delete()
    print(heap.arr)


if __name__ == "__main__":
    run()