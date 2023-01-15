L = {}

input = [x.strip() for x in open('d18.in').readlines()]

R = len(input)
C = len(input[0])

for r in range(R):
    for c in range(C):
        if input[r][c] == '#':
            L[(r, c)] = input[r][c]


for r, c in [(0, 0), (0, C-1), (R-1, 0), (R-1, C-1)]:
    L[(r, c)] = '#'


def next(r, c, L):
    on = 0

    if (r, c) in [(0, 0), (0, C-1), (R-1, 0), (R-1, C-1)]:
        return '#'

    for nr in [r-1, r, r+1]:
        for nc in [c-1, c, c+1]:
            if nr == r and nc == c:
                continue
            if 0 <= nr < R and 0 <= nc < C:
                if (nr, nc) in L and L[(nr, nc)] == '#':
                    on += 1

    if (r, c) in L and L[(r, c)] == '#':
        if on in [2, 3]:
            return '#'
        return '.'
    else:
        if on == 3:
            return '#'
        return '.'


for _ in range(100):
    LN = {}
    for r in range(R):
        for c in range(C):
            LN[(r, c)] = next(r, c, L)
    L = LN

print(sum([x == '#' for x in L.values()]))
