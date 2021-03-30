from graph import Node

def bfs(root):
  q = [root]
  visit = []
  while len(q):
    curr = q.pop(0)
    curr.visited = True
    visit.append(curr.value)
    for n in curr.children:
      if not n.visited:
        q.append(n)
  return ",".join(str(visit))

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)

node1.addChildren([node2, node3])
node2.addChildren([node4])
node3.addChildren([node4, node6])
node4.addChildren([])
node5.addChildren([node1, node2, node3])
node6.addChildren([node5])

print(bfs(node1))