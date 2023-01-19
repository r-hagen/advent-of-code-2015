instructions = [x.strip() for x in open('d23.in').readlines()]

R = {
    "a": 1,
    "b": 0
}

i = 0
while True:
    if i < 0 or i >= len(instructions):
        break

    parts = instructions[i].split()

    if len(parts) == 2:
        cmd, arg = parts
        if cmd == 'hlf':
            R[arg] = R[arg] // 2
            i += 1
        elif cmd == 'tpl':
            R[arg] = R[arg] * 3
            i += 1
        elif cmd == 'inc':
            R[arg] += 1
            i += 1
        elif cmd == 'jmp':
            offset = int(arg)
            i += offset
    else:
        cmd, reg, arg = parts
        offset = int(arg)
        reg = reg.strip(',')
        if cmd == 'jie' and R[reg] % 2 == 0:
            i += offset
        elif cmd == 'jio' and R[reg] == 1:
            i += offset
        else:
            i += 1

print(R['b'])
