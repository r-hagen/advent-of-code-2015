from functools import reduce
from itertools import combinations
from operator import mul

packages = [int(x.strip()) for x in open('d24.in').readlines()]
weight = sum(packages) // 4

for i in range(len(packages)):
    qes = [reduce(mul, c)
           for c in combinations(packages, i)
           if sum(c) == weight]
    if qes:
        print(min(qes))
        break
