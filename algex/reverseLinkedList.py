# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def reverseLinkedList(head):
		curr = head
		prev = None
		while curr is not None:
			follower = curr.next
			curr.next = prev
			prev = curr
			curr = follower
		return prev