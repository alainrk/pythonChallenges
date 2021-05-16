PUTTING = 0
GETTING = 1

class Queue:
  def __init__(self):
    self.stacks = [[], []]
    self.status = PUTTING
    self.currentStack = 0

  def _switchStackStatusAndPour(self):
    prevStack = self.currentStack
    self.currentStack = (self.currentStack + 1) % 2
    self.stacks[self.currentStack] = self.stacks[prevStack][::-1]
    self.stacks[prevStack] = []
    self.status = (self.status + 1) % 2

  def put(self, value):
    if self.status == GETTING:
      self._switchStackStatusAndPour()
    self.stacks[self.currentStack].append(value)

  def get(self):
    if self.status == PUTTING:
      self._switchStackStatusAndPour()
    return self.stacks[self.currentStack].pop()

  def current(self):
    if self.status == PUTTING:
      return self.stacks[self.currentStack]
    return self.stacks[self.currentStack][::-1]

q = Queue()
q.put(1)
q.put(2)
q.put(3)
q.put(4)

assert q.current() == [1, 2, 3, 4]
assert 1 == q.get()
assert q.current() == [2, 3, 4]

q.put(5)
q.put(6)

assert q.current() == [2, 3, 4, 5, 6]
assert 2 == q.get()
assert 3 == q.get()
assert 4 == q.get()
assert 5 == q.get()
assert 6 == q.get()

# Benching
# q = Queue()
# for i in range(10000):
#   for j in range(500):
#     q.put(1)
#     q.get()