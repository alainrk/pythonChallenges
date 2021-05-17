# This is the class of the input linked list.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def shiftLinkedList(head, k):
	if k == 0:
		return head
	nodes = {}
	i = 0
	curr = head
	tail = None
	while curr is not None:
		nodes[i] = curr
		i += 1
		tail = curr
		curr = curr.next
	k = k % i
	if k == 0:
		return head
	'''
	curr is the TAIL
	i is the length

	i = 6
	k = 2
	[0, 1, 2, 3, 4, 5]
	[4, 5, 0, 1, 2, 3]
	'''
	if k > 0:
		nodes[i - k -1].next = None
		tail.next = head
		head = nodes[i - k]
		return head
	'''
	i = 6
	k = -2
	[0, 1, 2, 3, 4, 5]
	[2, 3, 4, 5, 0, 1]
	'''
	nodes[-k - 1].next = None
	tail.next = head
	head = nodes[-k]
	return head


