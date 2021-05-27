# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

def insertAfter(node, newNode):
	newNode.next = node.next
	node.next = newNode

def zipLinkedList(head):
	prevs = {}
	curr = head
	prev = None

	while curr is not None:
		prevs[curr] = prev
		prev = curr
		curr = curr.next
	curr = head
	tail = prev

	while curr != tail and curr.next != tail:
		nextCurrent = curr.next
		insertAfter(curr, tail)

		if prevs[tail]:
			prevs[tail].next = None
		tail = prevs[tail]

		curr = nextCurrent
	return head