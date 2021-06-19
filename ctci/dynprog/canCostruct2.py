def canConstruct(bank, word):
  res = [False] * (len(word) + 1)
  res[0] = True

  for i in range(len(res)):
    if not res[i]:
      continue
    for bw in bank:
      chunk = word[i:i + len(bw)]
      if chunk == bw:
        aheadIdx = i + len(bw)
        res[aheadIdx] = True
  print(res)
  return res[len(word)]


# assert(canConstruct(['ab', 'abc', 'cd', 'def', 'abcd'], 'abcdef') == True)
assert(canConstruct(['fizz', 'buzz', 'fizzbuzz'], 'fizzbuzz') == True)
assert(canConstruct(['fizz', 'buzz'], 'fizzbuzz') == True)
assert(canConstruct(['a', 'aa', 'aaa', 'aaaa', 'aaaaa'], 'aaaaaaaaaaaaaaaaaaaaa') == True)
assert(canConstruct(['a', 'aa', 'aaa', 'aaaa', 'aaaaa'], 'aaaaaaaaaaaaaaaaaaaaab') == False)