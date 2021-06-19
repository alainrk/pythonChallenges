def canConstruct(bank, word):
  res = [False] * (len(word) + 1)
  res[0] = True

  '''
  Bank = 
  ['', a, ab, abc, abcd, abcde, abcdef]
  [T,  F,  F,   F,    F,     F,      F]
  '''
  for i in range(len(res)):
    for bw in bank:
      res[i] = word == word[:i] + bw
  return res[len(word)]

assert(canConstruct(['ab', 'abc', 'cd', 'def', 'abcd'], 'abcdef') == True)