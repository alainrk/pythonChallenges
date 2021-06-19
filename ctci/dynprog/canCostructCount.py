def canConstruct(bank, word):
  res = [0] * (len(word) + 1)
  res[0] = 1

  for i in range(len(res)):
    if not res[i]:
      continue
    for bw in bank:
      chunk = word[i:i + len(bw)]
      if chunk == bw:
        aheadIdx = i + len(bw)
        res[aheadIdx] += res[i]
  print(res)
  return res[len(word)]


assert(canConstruct(['ab', 'abc', 'cd', 'def', 'abcd'], 'abcdef') == 1)
assert(canConstruct(['fizz', 'buzz', 'fizzbuzz'], 'fizzbuzz') == 2)
assert(canConstruct(['fizz', 'buzz'], 'fizzbuzz') == 1)
assert(canConstruct(['a', 'a'], 'a') == 2)
assert(canConstruct(['purp', 'p', 'ur', 'le', 'purpl'], 'purple') == 2)