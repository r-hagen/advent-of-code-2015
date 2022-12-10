lines = [line.strip() for line in open('d06.in').readlines()]
G = [[0]*1000 for _ in range(1000)]
for line in lines:
    parts = line.split()
    if len(parts) == 4:
        cmd, start, _, end = parts
        x1, y1 = tuple(map(int, start.split(',')))
        x2, y2 = tuple(map(int, end.split(',')))
    else:
        cmd, val, start, _, end = parts
        x1, y1 = tuple(map(int, start.split(',')))
        x2, y2 = tuple(map(int, end.split(',')))
    for x in range(x1, x2+1):
        for y in range(y1, y2+1):
            if cmd == "toggle":
                G[y][x] += 2
            else:
                if val == "on":
                    G[y][x] += 1
                else:
                    G[y][x] -= 1
                    G[y][x] = max(0, G[y][x])
print(sum([G[y][x] for x in range(1000) for y in range(1000)]))
