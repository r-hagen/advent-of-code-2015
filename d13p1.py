import re

persons = set()
L = {}
for line in  [line.strip() for line in open('d13.in')]:
    p1, op, amt, p2 = re.match(r'(\w+) would (gain|lose) (\d+) happiness units by sitting next to (\w+)\.', line).groups()
    amt = int(amt)
    L[(p1, p2)] = amt if op == 'gain' else -amt
    persons.add(p1)
    persons.add(p2)

A = []
def permutate(seats=[]):
    if len(seats) == len(persons):
        h = 0
        for p1, p2 in zip(seats, seats[1:]):
            h += L[(p1, p2)] + L[(p2, p1)]
        h += L[(seats[0], seats[len(seats)-1])] + L[(seats[len(seats)-1], seats[0])]
        A.append((h, seats))
    for p in persons:
        if p not in seats:
            permutate(seats + [p])

permutate([])
print(max(A, key=lambda t: t[0])) 
