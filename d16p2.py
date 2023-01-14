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
cnt = 0

for line in lines:
    parts = line.split()
    id = parts[1][:-1]
    matches = 0

    i = 2
    while i < len(parts):
        prop = parts[i].strip(':')
        value = int(parts[i+1].strip(','))
        if prop in ['trees', 'cats'] and sue[prop] < value:
            matches += 1
        elif prop in ['pomeranians', 'goldfish'] and sue[prop] > value:
            matches += 1
        elif sue[prop] == value:
            matches += 1
        i += 2

    if matches == 3 and id != '213':
        ans = id
        break

    if matches > cnt:
        ans = id
        cnt = matches

print(ans)
