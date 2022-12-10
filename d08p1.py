import string

lines = [line.strip() for line in open('d08.in').readlines()]
s = 0
m = 0

for line in lines:
    s += len(line)

    t = []
    i = 0
    a = 0
    while i < len(line):
        c = line[i]
        if c == '\\':
            if line[i+1] == '\\':
                t.append('\\')
                i += 1
            elif line[i+1] == '"':
                t.append('"')
                i += 1
            elif line[i+1] == 'x' and line[i+2] in string.hexdigits and line[i+2] in string.hexdigits:
                t.append(chr(int(line[i+2:i+4], 16)))
                i += 3
        elif c == '"':
            t.append(c)
            a += 1
        else:
            t.append(c)
        i += 1

    t = ''.join(t)
    t = t.replace('"', '', a)

    m += len(t)

print(s-m)

# easy mode
print(sum(len(s[:-1]) - len(eval(s)) for s in open('d08.in')))
