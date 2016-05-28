def longest_palindrome (s):
    for i in reversed(range(1,len(s)+1)):
        for j in range(0,len(s)-i+1):
            if s[j:j+i] == (s[j:j+i])[::-1]:
                return i
    return 0

'''
"a" -> 1
"aab" -> 2
"abcde" -> 1
"zzbaabcd" -> 4
"" -> 0
'''
