from graph import Node

def kahn(nodes):
  incomings = {}

  for node in nodes:
    # incomings[node.value] = [n.value for n in node.children]
    for c in node.children:
      if not c.value in incomings:
        incomings[c.value] = {}
      incomings[c.value][node.value] = True

  topsort = []
  exitOnly = [n for n in nodes if n.value not in incomings]
  while len(exitOnly):
    curr = exitOnly.pop()
    topsort.append(curr.value)
    for m in curr.children:
      del incomings[m.value][curr.value]
      if len(incomings[m.value].keys()) == 0:
        exitOnly.append(m)
  return topsort


node5 = Node(5)
node7 = Node(7)
node3 = Node(3)
node11 = Node(11)
node8 = Node(8)
node2 = Node(2)
node9 = Node(9)
node10 = Node(10)

node5.addChildren([node11])
node7.addChildren([node11, node8])
node3.addChildren([node8, node10])
node11.addChildren([node2, node9, node10])
node8.addChildren([node9])
# node2.addChildren([])
# node9.addChildren([])
# node10.addChildren([])

nodes = []
nodes.append(node5)
nodes.append(node7)
nodes.append(node3)
nodes.append(node11)
nodes.append(node8)
nodes.append(node2)
nodes.append(node9)
nodes.append(node10)

print(kahn(nodes))