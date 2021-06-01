def run():
    heap = Heap()
    heap.insert(5)
    heap.insert(2)
    heap.insert(7)
    heap.insert(4)
    heap.insert(1)

    print(heap.arr)

    print(heap.delete())
    print(heap.arr)
    print(heap.delete())
    print(heap.arr)
    print(heap.delete())

class Heap:
    def __init__(self):
        self.arr = [0] * 11
        self.heap_size = 1

    def insert(self, x):
        idx = self.heap_size
        self.heap_size += 1

        while idx != 1 and x < self.arr[idx // 2]:
            self.arr[idx] = self.arr[idx // 2]
            idx //= 2

        self.arr[idx] = x

    def delete(self):
        return_val = self.arr[1]
        last_val = self.arr[self.heap_size - 1]
        self.arr[self.heap_size - 1] = 0
        self.heap_size -= 1

        parent = 1
        child = 2

        while child < self.heap_size:
            if self.arr[child] > self.arr[child + 1]:
                child += 1
            
            if self.arr[child] < self.arr[parent]: break
            self.arr[parent] = self.arr[child]
            parent = child
            child *= 2

        self.arr[parent] = last_val
        return return_val

if __name__ == "__main__":
    run()