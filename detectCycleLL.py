class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
        self.visited = False

    def setNext(self, next):
        self.next = next

    def detectLoop(self):
        print self.value
        if self.visited:
            print "LOOP!"
            return
        self.visited = True
        if self.next is not None:
            self.next.detectLoop()

root = Node(1)
a = Node(2)
b = Node(3)
c = Node(4)
root.setNext(a)
a.setNext(b)
b.setNext(c)
c.setNext(root)

root.detectLoop()
