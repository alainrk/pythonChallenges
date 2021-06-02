def splitInteger(num,parts):
  div, rest = num // parts, num % parts
  res = [div + (0 if i < (parts - rest) else 1) for i in range(parts)]
  return res

print(splitInteger(100, 9))


'''
def splitInteger(num,parts):
  div, rest = num // parts, num % parts
  res = [div + (1 if i < rest else 0) for i in range(parts)]
  return list(reversed(res)) # TODO Optimize this
  '''