def canConstruct(bank, word):
  res = [False] * (len(word) + 1)
  res[0] = True

  '''
  Bank = ['ab', 'abc', 'cd', 'def', 'abcd']

        ['', a, ab, abc, abcd, abcde, abcdef]
  res = [T,  F,  T,   F,    F,     F,      F]
         |   |   |
         |_ab|   |
         |_____ab|
  '''
  for i in range(len(res)):
    if not res[i]:
      continue
    for j in range(i + 1, len(res)):
      for bw in bank:
        # print(f'\'{word[:j]}\'', '==', word[:i], '+', bw, f', res[{word[:j]}] = {word[:j] == word[:i] + bw}')
        prefix = word[:i]
        currPartial = word[:j]
        itCan = currPartial == prefix + bw
        res[j] = res[j] or itCan # can be optimized exiting
  print(res)
  return res[len(word)]


assert(canConstruct(['ab', 'abc', 'cd', 'def', 'abcd'], 'abcdef') == True)
assert(canConstruct(['fizz', 'buzz', 'fizzbuzz'], 'fizzbuzz') == True)
assert(canConstruct(['fizz', 'buzz'], 'fizzbuzz') == True)
assert(canConstruct(['a', 'aa', 'aaa', 'aaaa', 'aaaaa'], 'aaaaaaaaaaaaaaaaaaaaa') == True)
assert(canConstruct(['a', 'aa', 'aaa', 'aaaa', 'aaaaa'], 'aaaaaaaaaaaaaaaaaaaaab') == False)