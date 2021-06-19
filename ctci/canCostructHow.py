def canConstruct(bank, word):
  res = [None] * (len(word) + 1)
  res[0] = [[]]

  for i in range(len(res)):
    if res[i] is None:
      continue
    for bw in bank:
      chunk = word[i:i + len(bw)]
      if chunk == bw:
        aheadIdx = i + len(bw)
        if res[aheadIdx] is None:
          res[aheadIdx] = []
        for arr in res[i]:
          res[aheadIdx].append(arr + [bw])
  print(res)
  return res[len(word)]


canConstruct(['ab', 'abc', 'cd', 'def', 'abcd'], 'abcdef')
canConstruct(['fizz', 'buzz', 'fizzbuzz'], 'fizzbuzz')
canConstruct(['fizz', 'buzz'], 'fizzbuzz')
canConstruct(['a', 'a'], 'a')
canConstruct(['a', 'a'], 'aa')
canConstruct(['purp', 'p', 'ur', 'le', 'purpl'], 'purple')