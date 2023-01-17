from collections import defaultdict

N = 33100000

house = defaultdict(int)

for i in range(1, N//10):
    for j in range(i, N//10, i):
        house[j] += i * 10

print(min([(i, c) for (i, c) in house.items() if (c >= N)]))
