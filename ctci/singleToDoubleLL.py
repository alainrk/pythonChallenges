from LinkedList import LinkedList

class DLinkedList(LinkedList):
  def __init__(self):
    super().__init__(False)
    self.tail = None

  def toDouble(self):
    prev = None
    curr = self.root
    while curr is not None:
      curr.prev = prev
      prev = curr
      curr = curr.next
    self.tail = prev

  def visitDouble(self):
    res = []
    curr = self.tail
    while curr is not None:
      res.append(curr.val)
      curr = curr.prev
    return res

ll = DLinkedList()
ll.add(1)
ll.add(2)
ll.add(3)
ll.add(4)
assert(len(ll) == 4)
assert(str(ll) == '1 2 3 4')

ll.toDouble()
res = ll.visitDouble()
assert(res == [4, 3, 2, 1])