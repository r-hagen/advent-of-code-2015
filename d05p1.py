lines = [string.strip() for string in open("d05.in").readlines()]
V = ['a', 'e', 'i', 'o', 'u']
F = ['ab', 'cd', 'pq', 'xy']

nice = 0
for s in lines:
    f = False
    v = 0
    d = False
    for x in F:
        if x in s:
            f = True
            break
    for c in s:
        if c in V:
            v += 1
    for a, b in zip(s, s[1:]):
        if a == b:
            d = True
            break
    if v >= 3 and d and not f:
        nice += 1
print(nice)
