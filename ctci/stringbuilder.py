class StringBuilder:
  def __init__(self):
    self.strings = []

  def add(self, str):
    self.strings.append(str)

  def toString(self):
    return "".join(self.strings)

sb = StringBuilder()
sb.add('This ')
sb.add('is ')
sb.add('a ')
sb.add('test!')
assert ("This is a test!" == sb.toString())

sb = StringBuilder()
assert ("" == sb.toString())

print('Tests are ok')