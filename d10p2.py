def lns(s, count=1):
    m = []
    c, cc = s[0], 1
    i = 1
    while i < len(s):
        if s[i] == c:
            cc += 1
        else:
            m.append([c, cc])
            c = s[i]
            cc = 1
        i += 1
    m.append([c, cc])
    r = ''
    for c, cc in m:
        r += str(cc)
        r += str(c)
    return r

ans = '1321131112'
for _ in range(50):
    ans = lns(ans)
    
print(len(ans))
