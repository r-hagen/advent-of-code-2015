import hashlib
s = "bgvyzdsv"
for n in range(pow(10, 6)):
    n = str(n).zfill(5)
    md5 = hashlib.md5((s+n).encode()).hexdigest()
    if md5.startswith('00000'):
        print(n)
        break

