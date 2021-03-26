class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

class LinkedList:
  def __init__(self, isReversed = False):
    self.root = None
    self.last = None
    self.isReversed = isReversed
    self.length = 0

  def __len__(self):
    return self.length

  def __str__(self):
    visit = []
    curr = self.root
    while curr is not None:
      visit.append(str(curr.val))
      curr = curr.next
    return " ".join(visit)

  # key = None to get the first item
  def get(self, val):
    curr = self.root
    while curr is not None:
      if curr.val == val:
        return curr
      curr = curr.next

  def delete(self, val):
    if self.root is None:
      return None

    curr = self.root

    if curr.val == val:
      self.root = curr.next
      self.length -= 1

    while curr.next is not None:
      if curr.next.val == val:
        curr.next = curr.next.next
        self.length -= 1
        return
      curr = curr.next

  def add(self, val):
    newNode = Node(val)

    if self.isReversed:
      newNode.next = self.root
      self.root = newNode
    else:
      if self.last:
        self.last.next = newNode

    if not self.isReversed:
      self.last = newNode

    if self.length == 0:
      self.root = newNode
      self.last = newNode
    self.length += 1


ll = LinkedList()
ll.add(1)
ll.add(2)
ll.add(3)
ll.add(4)
assert(len(ll) == 4)
assert(str(ll) == '1 2 3 4')

llRev = LinkedList(True)
llRev.add(1)
llRev.add(2)
llRev.add(3)
llRev.add(4)
assert(len(llRev) == 4)
assert(str(llRev) == '4 3 2 1')