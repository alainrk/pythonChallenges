# This is an input class. Do not edit.
class LinkedList:
  def __init__(self, value):
    self.value = value
    self.next = None

# e.g. 18 => (1, 8)
def splitDecAndUnits(num):
	return num // 10, num % 10

def sumOfLinkedLists(c1, c2):
  newll = LinkedList(0) # mock
  currll = newll
  remainder = 0

  while c1 is not None or c2 is not None or remainder != 0:
    v1 = c1.value if c1 is not None else 0
    v2 = c2.value if c2 is not None else 0
    c1 = c1.next if c1 is not None else None
    c2 = c2.next if c2 is not None else None

    remainder, units = splitDecAndUnits(v1 + v2 + remainder)
    currll.next = LinkedList(units)
    currll = currll.next

  # in case the sum is just 0
  if newll is None:
    return currll
  # mock next is the real head
  return newll.next

