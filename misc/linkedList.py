class Node:
  def __init__(self, val, next = None):
    self.val = val
    self.next = next

class LinkedList:
  def __init__(self, root):
    self.root = root

  def visit(self):
    curr = self.root
    while curr is not None:
      print(curr.val)
      curr = curr.next

  def reverse (self):
    prev = None
    curr = self.root
    while curr is not None:
      next = curr.next
      curr.next = prev
      prev = curr
      curr = next
    self.root = prev

root = Node(
  10,
  Node(9,
    Node(8,
      Node(7,
        Node(6)
      )
    )
  )
)

ll = LinkedList(root)
ll.reverse()
ll.visit()