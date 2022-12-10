lines = [line.strip() for line in open('d06.in').readlines()]
G = [[False]*1000 for _ in range(1000)]
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
                G[y][x] = not G[y][x]
            else:
                if val == "on":
                    G[y][x] = True
                else:
                    G[y][x] = False
print(sum([1 if G[y][x] else 0 for x in range(1000) for y in range(1000)]))
