def mix(s1, s2, whos={},reps={}):
    result=[]
    s1,s2 = ({l:s.count(l) for l in set(s) if l.islower() and s.count(l)>1} for s in (s1,s2))
    for l in set(s1.keys()).union(set(s2.keys())):
        oneReps, twoReps = (s.get(l,-1) for s in (s1,s2))
        maxreps = max(oneReps,twoReps)
        whomax = "1" if oneReps > twoReps else ("2" if twoReps > oneReps else "=")
        whos[l] = whomax
        if reps.get(maxreps,-1) == -1:
            reps[maxreps] = []
        reps[maxreps].append(l)

    while reps:
        maxr = max(reps)
        letters = reps[maxr]
        part = []
        for l in letters:
            part += ["{}:{}".format(whos[l],l*maxr)]
        part.sort()
        result += part
        del reps[maxr]
    return "/".join(result)
    
print mix("looqqqqqpingaaaa is fun but dangerous", "less daangeroqqqqus thaaan coding")
print mix(" In many languages", " there's a pair of functions")
