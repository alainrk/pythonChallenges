def canConstruct(bank, word):
  res = [[] for _ in range(len(word) + 1)]
  res[0].append([])

  for i in range(len(res)):
    if len(res[i]) == 0:
      continue
    for bw in bank:
      chunk = word[i:i + len(bw)]
      if chunk == bw:
        aheadIdx = i + len(bw)
        for arr in res[i]:
          res[aheadIdx].append(arr + [bw])
  print(res)
  return res[len(word)]


canConstruct(['ab', 'abc', 'cd', 'def', 'abcd'], 'abcdef')
canConstruct(['ab', 'abc', 'cd', 'def', 'abcd', 'ef', 'c'], 'abcdef')
canConstruct(['fizz', 'buzz', 'fizzbuzz'], 'fizzbuzz')
canConstruct(['fizz', 'buzz'], 'fizzbuzz')
canConstruct(['a', 'a'], 'a')
canConstruct(['a', 'a'], 'aa')
canConstruct(['purp', 'p', 'ur', 'le', 'purpl'], 'purple')