import hashlib
s = "bgvyzdsv"
for n in range(pow(10, 7)):
    n = str(n).zfill(6)
    md5 = hashlib.md5((s+n).encode()).hexdigest()
    if md5.startswith('000000'):
        print(n)
        break

