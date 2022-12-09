S = R = (0, 0)
DX = {"<": -1, ">": 1, "^": 0, "v": 0}
DY = {"<": 0, ">": 0, "^": 1, "v": -1}
v = set()
v.add(S)
k = 0
for c in open("d03.in").readline().strip():
    if k % 2 == 0:
        S = (S[0]+DX[c], S[1]+DY[c])
        v.add(S)
    else:
        R = (R[0]+DX[c], R[1]+DY[c])
        v.add(R)
    k += 1
print(len(v))
