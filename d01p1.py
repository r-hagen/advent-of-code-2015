ans = 0
M = {"(": 1, ")": -1}
for c in open("d01.in").readline().strip():
    ans += M[c]
print(ans)

