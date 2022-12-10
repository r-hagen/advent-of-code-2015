lines = [line.strip() for line in open('d07.in').readlines()]

W = {}
for line in lines:
    cmd, w = line.split(' -> ')
    parts = cmd.split()
    W[w] = parts

def signal(w):
    if isinstance(w, int) or w.isnumeric():
        return int(w)
    elif len(W[w]) == 1:
        return signal(W[w][0])
    elif len(W[w]) == 2:
        return ~signal(W[w][1])

    x, op, y = W[w]
    if op == 'AND':
        W[w] = [signal(x) & signal(y)]
    elif op == 'OR':
        W[w] = [signal(x) | signal(y)]
    elif op == 'LSHIFT':
        W[w] = [signal(x) << int(y)]
    elif op == 'RSHIFT':
        W[w] = [signal(x) >> int(y)]

    return W[w][0]

sa = signal('a')

W = {}
for line in lines:
    cmd, w = line.split(' -> ')
    parts = cmd.split()
    W[w] = parts

W['b'] = [sa]
print(signal('a'))
