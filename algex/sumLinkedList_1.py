# This is an input class. Do not edit.
class LinkedList:
  def __init__(self, value):
    self.value = value
    self.next = None

# e.g. 18 => (1, 8)
def splitDecAndUnits(num):
	remainder = (num // 10)
	units = num - (remainder * 10)
	return remainder, units

def sumOfLinkedLists(c1, c2):
  newll = None
  currll = None
  remainder = 0

  while True:
    currSum = remainder
    if c1 is not None:
      currSum += c1.value
      c1 = c1.next
    if c2 is not None:
      currSum += c2.value
      c2 = c2.next
    remainder, units = splitDecAndUnits(currSum)

    if not c1 and not c2 and remainder + units == 0:
      break

    # Set new linkedlist head
    if newll is None:
      newll = LinkedList(units)
      currll = newll
    else:
      currll.next = LinkedList(units)
      currll = currll.next

  if newll is None:
    return LinkedList(0)
  return newll
