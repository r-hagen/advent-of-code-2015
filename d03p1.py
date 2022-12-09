P = (0, 0)
DX = {"<": -1, ">": 1, "^": 0, "v": 0}
DY = {"<": 0, ">": 0, "^": 1, "v": -1}
v = set()
v.add(P)
for c in open("d03.in").readline().strip():
    P = (P[0]+DX[c], P[1]+DY[c])
    v.add(P)
print(len(v))
