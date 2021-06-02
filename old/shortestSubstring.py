def shortest(dio):
    d = {}
    d["a"], d["b"], d["c"] = -1, -1, -1
    start, end = 0, len(dio)

    for i, v in enumerate(dio):
        # print i, v, start, end
        d[v] = i
        if d["a"] > 0 and d["b"] > 0 and d["c"] > 0:
            s, e = min(d["a"], d["b"], d["c"]), max(d["a"], d["b"], d["c"]) # TODO Optimize in only a cycle
            if e-s < end-start:
                start, end = s, e
    print start, end
    return dio[start:end+1]

print shortest("babdfguyihojcalkkghkja56f6ghujiokhgfdbfjhkhcabbb")
print shortest("baaaaaaaac")
