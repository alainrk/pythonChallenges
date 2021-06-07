# This is an input class. Do not edit.
class Node:
	def __init__(self, value):
		self.value = value
		self.prev = None
		self.next = None

class DoublyLinkedList:
	def __init__(self):
		self.head = None
		self.tail = None

def setHead(self, node):
	if self.head is None:
		self.head = node
		self.tail = node
		return
	self.insertBefore(self.head, node)

def setTail(self, node):
	if self.tail is None:
		self.setHead(node)
		return
	self.insertAfter(self.tail, node)

def insertBefore(self, node, nodeToInsert):
	if self.head == nodeToInsert == self.tail:
		return

	self.remove(nodeToInsert)
	nodeToInsert.next = node
	nodeToInsert.prev = node.prev
	if node.prev is None:
		self.head = nodeToInsert
	else:
		node.prev.next = nodeToInsert
	node.prev = nodeToInsert

def insertAfter(self, node, nodeToInsert):
	if self.head == nodeToInsert == self.tail:
		return

	self.remove(nodeToInsert)
	nodeToInsert.prev = node
	nodeToInsert.next = node.next
	if node.next is None:
		self.tail = nodeToInsert
	else:
		node.next.prev = nodeToInsert
	node.next = nodeToInsert

def insertAtPosition(self, position, nodeToInsert):
	if position == 1:
		self.setHead(nodeToInsert)
		return

	# TODO Maybe optimizable with double pointer (using tail)
	curr = self.head
	# while position > 1 and curr is not None:
	cp = 1
	while curr is not None and cp != position:
		curr = curr.next
		cp += 1

		if curr is not None:
			self.insertBefore(curr, nodeToInsert)
			return
		self.setTail(nodeToInsert)

def removeNodesWithValue(self, value):
	curr = self.head
	while curr is not None:
		n = curr
		curr = curr.next
		if n.value == value:
			self.remove(n)

def remove(self, node):
	if self.head == node:
		self.head = node.next
	if self.tail == node:
		self.tail = node.prev
	if node.prev:
		node.prev.next = node.next
	if node.next:
		node.next.prev = node.prev
	node.prev = node.next = None

def containsNodeWithValue(self, value):
	h, t = self.head, self.tail
	while h != t:
		if h.value == value or t.value == value:
			return True
		h, t = h.next, t.prev
	return False