from copy import deepcopy
from collections import defaultdict


M = {}
for line in open('d15.in').readlines():
    parts = line.split()
    name = parts[0][:-1]
    cap = int(parts[2][:-1])
    dur = int(parts[4][:-1])
    fla = int(parts[6][:-1])
    tex = int(parts[8][:-1])
    cal = int(parts[10])
    M[name] = (cap, dur, fla, tex, cal)


def score(I):
    c = d = f = t = 0

    for i, a in I.items():
        c += M[i][0] * a
        d += M[i][1] * a
        f += M[i][2] * a
        t += M[i][3] * a

    c = max(0, c)
    d = max(0, d)
    f = max(0, f)
    t = max(0, t)

    return c*d*f*t


DP = {}
def f(I, t):
    if t == 0:
        return score(I)

    key = tuple(sorted(I.items()))
    if key in DP:
        return DP[key]
     
    ans = 0
    for ing in M.keys():
        nI = deepcopy(I)
        nI[ing] += 1
        ans = max(ans, f(nI, t-1))

    DP[key] = ans

    # if len(DP) % 10000 == 0:
    #     print(len(DP))

    return ans

ans = f(defaultdict(int), 100)
print(ans)
