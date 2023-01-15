_, molecule = [x.strip() for x in open('d19.in').read().split('\n\n')]

p1 = sum(1 for x in molecule if str.isupper(x))
p2 = molecule.count('Rn') + molecule.count('Ar')
p3 = molecule.count('Y')

print(p1 - p2 - 2*p3 - 1)
