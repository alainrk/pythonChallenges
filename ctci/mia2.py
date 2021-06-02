def string_suffix(str):
  start, end = 0, 0
  count = 0
  similarity = 0
  while end < len(str):
    count += 1
    cut = 0
    while cut < count:
      pre = str[start:end + 1 - cut]
      suf = str[-count:len(str) - cut]

      if pre == suf:
        similarity += (count - cut)
        break

      cut += 1
    end += 1
  return similarity

print(string_suffix('ababaa'))