lines = [line.strip() for line in open('d08.in').readlines()]
o = 0
e = 0

for line in lines:
    o += len(line)
    t = ''
    i = 0
    while i < len(line):
        c = line[i]
        if c == '"':
            t += '\\"'
        elif c == '\\':
            t += '\\\\'
        else:
            t += c
        i += 1
    t = '"' + t + '"'
    e += len(t)

print(e-o)

# easy mode
print(sum(2+s.count('\\')+s.count('"') for s in open('d08.in')))

