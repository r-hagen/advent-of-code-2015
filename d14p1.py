import re

reindeer = [line.strip() for line in open('d14.in').readlines()]

SPEED = 0
FLYDUR = 1
RESTDUR = 2
DISTANCE = 3
FLYING = 4
RESTING = 5
MODE = 6

R = {}
for r in reindeer:
    name, speed, fly, rest = re.search(r'(\w+) .* (\d+) km/s for (\d+) seconds, .* (\d+) seconds', r).groups()
    R[name] = [int(speed), int(fly), int(rest), 0, 0, 0, 'fly']

t = 1
while True:
    for name, data in R.items():
        if data[MODE] == 'fly': 
            if data[FLYING] < data[FLYDUR]:
                data[DISTANCE] += data[SPEED]
                data[FLYING] += 1
            else:
                data[MODE] = 'rest'
                data[RESTING] = 1
        else:
            if data[RESTING] < data[RESTDUR]:
                data[RESTING] += 1
            else:
                data[MODE] = 'fly'
                data[FLYING] = 1
                data[DISTANCE] += data[SPEED]
    if t == 2503:
        print(max([x[DISTANCE] for x in R.values()]))
        break
    t += 1

