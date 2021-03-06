"""
Hackerrank

Lexicographical order is often known as alphabetical order when dealing with strings. A string is greater than another string if it comes later in a lexicographically sorted list.

Given a word, create a new word by swapping some or all of its characters. This new word must meet two criteria:

It must be greater than the original word
It must be the smallest word that meets the first condition

abc => [acb, bac, bca, cba, cab] => Result: acb

1. Bruteforce: permutaton, get the min
  1a. Bruteforce, permutations pruning the lower ones, get the min

"""

def minGreater(w):
  original = list(w)
  for i in range(len(original) - 2, -1, -1):
    minAmongGreater = None
    minAmongGreaterIndex = None
    for j in range(i + 1, len(original)):
      # Find the number that's the minimum among the greater than the current w[i]
      if original[i] < original[j] and (minAmongGreater is None or original[j] < minAmongGreater):
        minAmongGreater = original[j]
        minAmongGreaterIndex = j
    if minAmongGreater is not None:
      firstPart = original[:i]
      central = [minAmongGreater]
      secondPart = sorted(original[i:minAmongGreaterIndex] + original[minAmongGreaterIndex+1:len(original)])
      return "".join(firstPart + central + secondPart)
  return "no answer"

def solve(w):
  result = [minGreater(x) for x in w.split('\n')]
  return "\n".join(result)

input = """lmno
dcba
dcbb
abdc
abcd
fedcbabcd"""

expected = """lmon
no answer
no answer
acbd
abdc
fedcbabdc"""

output = solve(input)
print(output)
assert output == expected