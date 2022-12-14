import re
input = open('d12.in').read().strip()
print(sum(list(map(int, re.findall(r'-*\d+', input)))))
