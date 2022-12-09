lines = [line.strip() for line in open("d02.in").readlines()]
ans = 0
for line in lines:
    l, w, h = map(int, line.split("x"))
    a = [l*w, w*h, h*l]
    s = min(a)
    ans += 2*a[0] + 2*a[1] + 2*a[2] + s
print(ans)

