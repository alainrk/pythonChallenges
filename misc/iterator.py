class EvenNums:
  def __init__(self, maxn):
    self.curr = 0
    self.maxn = maxn

  def __iter__(self):
    return self

  def __next__(self):
    self.curr += 2
    if self.curr > self.maxn:
      raise StopIteration
    return self.curr

e = EvenNums(40)
print(sum(e))