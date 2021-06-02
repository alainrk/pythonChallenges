class Node:
    def __init__(self, value):
        self.value = value
        self.neighbours = []
        self.visited = False

def bfs(root):
    q = []
    q.append(root)
    root.visited = True
    print root.value

    while (len(q) > 0):
        curr = q.pop()
        for n in curr.neighbours:
            if not n.visited:
                print n.value
                n.visited = True
                q.append(n)

root = Node(0)
a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)
f = Node(6)

root.neighbours = [a,c]
a.neighbours = [root,b]
b.neighbours = [f]
c.neighbours = [root,c]
d.neighbours = [c,e,f]
e.neighbours = [d,f]
f.neighbours = [d,e,b]

bfs(root)
