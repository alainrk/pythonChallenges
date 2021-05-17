# This is the class of the input linked list.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def shiftLinkedList(head, k):
	length = 1
	tail = head
	while tail.next is not None:
		length += 1
		tail = tail.next

	offset = abs(k) % length
	if offset == 0:
		return head

	'''
	[0, 1, 2, 3, 4, 5]
	k = 2 => [4, 5, 0, 1, 2, 3] # offset = 6 - |2| = 4
	k = -2 => [2, 3, 4, 5, 0, 1] # offset = |-2| = 2
	'''
	newTailIndex = length - offset if k > 0 else offset
	newTail = head
	for i in range(newTailIndex - 1):
		newTail = newTail.next

	tail.next = head
	head = newTail.next
	newTail.next = None
	return head


