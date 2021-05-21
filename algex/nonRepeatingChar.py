import math

# T O(n) | S O(1) [Max english alphabet]
def firstNonRepeatingCharacter(string):
  chars = {}
  for i, c in enumerate(string):
    chars[c] = math.inf if c in chars else i

  maxi = math.inf
  for v in chars.values():
    maxi = min(v, maxi)
    return -1 if maxi > len(string) else maxi
