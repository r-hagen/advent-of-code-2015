t, m = [x.strip() for x in open('d19.in').read().split('\n\n')]

R = []
for r in t.split('\n'):
    f, t = r.split(' => ')
    R.append((f, t))

M = set()
for f, t in R:
    i = 0
    while i < len(m):
        if m[i:i+len(f)] == f:
            r = m[0:i] + t + m[i+len(f):len(m)]
            M.add(r)
        i += 1

print(len(M))
