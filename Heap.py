class Heap:
    def __init__(self):
        self.arr = [0, ]
        self.heap_size = 1

    def insert(self, x):
        self.arr.append(x)

        cnt = self.heap_size
        while cnt != 1:
            if self.arr[cnt] > self.arr[cnt // 2]:
                tmp = self.arr[cnt]
                self.arr[cnt] = self.arr[cnt // 2]
                self.arr[cnt // 2] = tmp
                cnt //= 2

            else:
                break

        self.heap_size += 1

    def delete(self):
        value = self.arr[1]
        self.arr[1] = self.arr[-1]

        cnt = 1
        while cnt <= self.heap_size:
            largest_idx = 0
            if cnt < self.heap_size and self.arr[cnt] > self.arr[cnt + 1]:
                largest_idx = cnt
            else:
                largest_idx = cnt + 1
            
            

        return value

def run():
    heap = Heap()
    heap.insert(5)
    heap.insert(7)
    print(heap.arr)

if __name__ == "__main__":
    run()