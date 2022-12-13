def valid(pwd):
    invalid = ['i', 'o', 'l']
    straight = False
    pairs = set()
    for a, b, c in zip(pwd, pwd[1:], pwd[2:]):
        if a in invalid or b in invalid or c in invalid:
            return False
        if a == b:
            pairs.add(a)
        if b == c:
            pairs.add(b)
        if ord(a) == ord(b)-1 and ord(b) == ord(c)-1:
            straight = True
    if len(pairs) < 2:
        return False
    if not straight:
        return False
    return True

def next(pwd):
    p = list(pwd)
    i = len(p) - 1
    while True:
        p[i] = chr(ord(p[i])+1) if p[i] != 'z' else 'a'
        if p[i] == 'a':
            i -= 1
        elif valid(p):
            return ''.join(p)
        else:
            i = len(p) - 1

p1 = next('vzbxkghb')
p2 = next(p1)
print(p1, p2)
