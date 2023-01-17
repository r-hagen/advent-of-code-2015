from collections import defaultdict

N = 33100000

presents = defaultdict(int)
delivered = defaultdict(int)

for elf in range(1, N//11):
    for house in range(elf, N//11, elf):
        if delivered[elf] >= 50:
            break
        presents[house] += elf * 11
        delivered[elf] += 1

print(min([(i, c) for (i, c) in presents.items() if (c >= N)]))
