lines = [x.strip() for x in open('d16.in').readlines()]

sue = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1,
}

ans = 0
mcnt = 0

for line in lines:
    parts = line.split()
    id = parts[1][:-1]
    matches = 0

    i = 2
    while i < len(parts):
        p = parts[i].strip(':')
        c = int(parts[i+1].strip(','))
        if sue[p] == c:
            matches += 1
        i += 2

    if matches > mcnt:
        ans = id
        mcnt = matches

print(ans)
