lines = [line.strip() for line in open("d02.in").readlines()]
ans = 0
for line in lines:
    l, w, h = list(map(int, line.split("x")))
    perimeter = lambda a, b: 2*a + 2*b
    m = min([(l, w), (w, h), (h, l)], key=lambda t: perimeter(t[0], t[1]))
    ans += 2*m[0]+2*m[1] + l*w* h
print(ans)

