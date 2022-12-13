import re
from collections import defaultdict

lines = [line.strip() for line in open('d09.in')]

L = defaultdict(set)
for line in lines:
    f, t, c = re.match(r'(\w+) to (\w+) = (\d+)', line).groups()
    c = int(c)
    L[f].add((t, c))
    L[t].add((f, c))

R = []
def permutate(route, cost=0):
    if len(route) == len(L):
        R.append((cost, route))
    else:
        for d, c in L[route[len(route)-1]]:
            if d not in route:
                permutate(route + [d], cost + c)

for start in L.keys():
    permutate([start])

print(min(R, key=lambda t: t[0]))
