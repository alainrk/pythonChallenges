def left(index):
    return 2 * index + 1

def right(index):
    return 2 * index + 2

def parent(index):
    return (index - 1) // 2

# i => L: 2i+1 R: 2i+2
# 0 => 1, 2 | 1 => 3, 4 | 2 => 5, 6 | ...
class MinHeap:
    def __init__(self, array):
        self.heap = self.buildHeap(array)

    def buildHeap(self, array):
        self.heap = []
        for item in array:
            self.heap.append(item)
            self.siftUp()
        return self.heap

    def siftDown(self):
        curr = 0
        while True:
            l, r = left(curr), right(curr)
            minimum = curr if l >= len(self.heap) or self.heap[curr] < self.heap[l] else l
            minimum = minimum if r >= len(self.heap) or self.heap[minimum] < self.heap[r] else r
            if minimum == curr:
                return
            self.heap[minimum], self.heap[curr] = self.heap[curr], self.heap[minimum]
            curr = minimum

    def siftUp(self):
        curr = len(self.heap) - 1
        while curr > 0:
            currVal = self.heap[curr]
            parentVal = self.heap[parent(curr)]
            if parentVal > currVal:
                self.heap[curr], self.heap[parent(curr)] = self.heap[parent(curr)], self.heap[curr]
                curr = parent(curr)
            else:
                break

    def remove(self):
        self.heap[0], self.heap[len(self.heap) - 1], = self.heap[len(self.heap) - 1], self.heap[0]
        res = self.heap.pop()
        self.siftDown()
        return res

    def peek(self):
        return self.heap[0]

    def insert(self, value):
        self.heap.append(value)
        self.siftUp()
