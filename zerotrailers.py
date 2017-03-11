def transform(s):
    t, c = [], 0
    for i in s:
        if i != 0:
            t.append(i)
        else:
            c += 1
    return [0 for x in xrange(c)] + t

def transform2(s):
    c = 0
    for i in xrange(len(s)):
        if s[i] != 0:
            s.append(s[i])
            s[i] = 0
            c+=1
    return s[c:]

print transform([0,0,0,0,30,0,0,0,2,0,0,5,6,20,0,0,0,0,0,0])
print transform2([0,0,0,0,30,0,0,0,2,0,0,5,6,20,0,0,0,0,0,0])
