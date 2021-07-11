# This is an input class. Do not edit.
class LinkedList:
  def __init__(self, value):
    self.value = value
    self.next = None


def mergeLinkedLists(headOne, headTwo):
	a, b = headOne, headTwo
	prev = None
	while a is not None and b is not None:
		if a.value <= b.value:
			prev = a
			a = a.next
			continue
		# if a.value > b.value
		bfollow = b.next
		if prev is None:
			headOne = b
		else:
			prev.next = b
		b.next = a
		prev = b
		b = bfollow
	if a is None:
		prev.next = b
	return headOne
