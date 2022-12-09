lines = [string.strip() for string in open("d05.in").readlines()]
nice = 0
for s in lines:
    r = False
    for a, b, c in zip(s, s[1:], s[2:]):
        if a == c:
            r = True
            break

    t = {}
    for i in range(len(s)-1):
        a, b = s[i], s[i+1]
        if a+b in t:
            t[a+b].append(i)
            t[a+b].append(i+1)
        else:
            t[a+b] = [i, i+1]


    tt = [len(set(v)) >= 4 for _, v in t.items()]
    if r and any(tt):
        nice += 1
print(nice)
