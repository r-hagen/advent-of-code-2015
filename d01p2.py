ans = 0
p = 0
M = {"(": 1, ")": -1}
for c in open("d01.in").readline().strip():
    p += 1
    ans += M[c]
    if ans == -1:
        break
print(p)

