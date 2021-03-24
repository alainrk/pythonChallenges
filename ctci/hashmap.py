import hashlib

class Node:
  def __init__(self, key, val):
    self.key = key
    self.val = val
    self.next = None

class LinkedListReverse:
  def __init__(self):
    self.root = None
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
  def get(self, key = None):
    curr = self.root
    while curr is not None:
      if key is None or curr.key == key:
        return curr.val
      curr = curr.next

  def delete(self, key):
    if self.root is None:
      return None

    curr = self.root

    if curr.key == key:
      self.root = curr.next

    while curr.next is not None:
      if curr.next.key == key:
        curr.next = curr.next.next
        return
      curr = curr.next

  def add(self, node):
    node.next = self.root
    self.root = node
    self.length += 1

class HashMap:
  def __init__(self, length = 65536):
    self.conflicts = 0
    self.length = length
    self.hashmap = [LinkedListReverse() for x in range(self.length)]

  def __calcIndex(self, key):
    # Hash the encoded key and take the binary
    # Only pick the first 18 chars
    # Hex to int
    # Module of the total length
    return int(hashlib.sha256(key.encode('utf-8')).hexdigest()[:18], 16) % self.length

  def get(self, key):
    index = self.__calcIndex(key)
    lookupVal = self.hashmap[index].get(key)
    return lookupVal

  def delete(self, key):
    index = self.__calcIndex(key)
    self.hashmap[index].delete(key)

  def add(self, key, val):
    index = self.__calcIndex(key)
    if len(self.hashmap[index]) > 0:
      self.conflicts += 1
    self.hashmap[index].add(Node(key, val))

  def add_optimized(self, key, val):
    index = self.__calcIndex(key)
    for i in range(self.length):
      if len(self.hashmap[index]) == 0:
        break
      if i < (self.length - 1):
        index = (index + 1) % self.length
        continue
      self.conflicts += 1
    self.hashmap[index].add(Node(key, val))

# ll = LinkedListReverse()
# ll.add(Node(1, 1))
# ll.add(Node(2, 2))
# ll.add(Node(3, 3))
# ll.add(Node(4, 4))

# ll.delete(2)
# ll.delete(4)
# assert (str(ll) == '3 1')
# ll.delete(1)
# ll.delete(3)
# assert (str(ll) == '')

# print('LinkedList Tests are ok')

# hm = HashMap()
# hm.add('key', 234)
# hm.add('koy', 'Value')
# hm.add('foo', 666)
# hm.add('fee', { "asd": 123 })
# hm.add('bar', [1, 2, 3])

# assert (hm.get('key') == 234)
# assert (len(hm.get('bar')) == 3)

# hm.delete('koy')
# assert (hm.get('koy') is None)

# print('Hashmap Tests are ok')