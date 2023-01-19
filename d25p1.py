row = 2978
col = 3083

code = 20151125
codes = sum(range(row + col - 1)) + col

for _ in range(codes - 1):
    code = (code * 252533) % 33554393

print(code)
