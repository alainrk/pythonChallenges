'''
S(x) = [a, b, c]
S(num) = [c(num[0]_0) + S(num[1:]), c(num[0]_1) + S(num[1:]), ...]
'''

memo = {
  "1": ['1'],
  "2": ['a', 'b', 'c'],
  "3": ['d', 'e', 'f'],
  "4": ['g', 'h', 'i'],
  "5": ['j', 'k', 'l'],
  "6": ['m', 'n', 'o'],
  "7": ['p', 'q', 'r', 's'],
  "8": ['t', 'u', 'v'],
  "9": ['w', 'x', 'y', 'z'],
  "0": ['0']
}

def phoneNumberMnemonics(phoneNumber):
  if phoneNumber in memo:
    return memo[phoneNumber]

  result = []
  fwd = phoneNumberMnemonics(phoneNumber[1:])
  for c in memo[phoneNumber[0]]:
    for f in fwd:
      result.append(c + f)
  return result

phoneNumberMnemonics('3485932093840223')
# print(memo)